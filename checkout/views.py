from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from products.models import Product
from .models import Booking
from .forms import BookingForm

import stripe


def checkout(request, product_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rental_days = int(request.POST.get('rentDays'))
    total_cost = int(product.price * rental_days)
    stripe_total = round(total_cost * 100)

    if request.method == 'POST':
        form_data = {
            # 'full_name': request.POST['full_name'],
            # 'email': request.POST['email'],
            # 'phone_number': request.POST['phone_number'],
            # 'postcode': request.POST['postcode'],
            # 'town_or_city': request.POST['town_or_city'],
            # 'street_address1': request.POST['street_address1'],
            # 'street_address2': request.POST['street_address2'],
            # 'county': request.POST['county'],
            'start_date': request.POST['startDate'],
            'rental_days': request.POST['rentDays'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            booking.stripe_pid = pid
            booking.product = product
            booking.product_size = product.size
            booking.start_date = start_date
            booking.rental_days = rental_days
            booking.save()

            return redirect(reverse(
                'checkout_success', args=[booking.booking_number]))
        else:
            messages.error(request, 'There was an error with your booking.\
                Please double check your information and try again.')
    else:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not rental_days:
            messages.error(request, "You haven't selected rental dates!")
            return redirect(reverse('products'))

        booking_form = BookingForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'product': product,
        'start_date': start_date,
        'rental_days': rental_days,
        'total_cost': total_cost,
        'stripe_total': stripe_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, booking_number):
    """ Handle successful checkouts """
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Order successfully processed! \
        Your booking number is {booking_number}. A confirmation \
        email will be sent to {booking.email}.')

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)
