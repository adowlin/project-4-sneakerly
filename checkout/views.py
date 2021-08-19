from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from products.models import Product
from .models import Booking, BookingLineItem
from .forms import BookingForm
from bag.contexts import bag_contents

import stripe
import json


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        current_bag = bag_contents(request)
        total_cost = current_bag['total_cost']

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'total_cost': total_cost,
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    booking_line_item = BookingLineItem(
                                booking=booking,
                                product=product,
                                rental_days=item_data,
                            )
                    booking_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "The product in your bag wasn't "
                        "found in our database. "
                        "Please email us for assistance!")
                    )
                    booking.delete()
                    return redirect(reverse('bag'))

            return redirect(reverse(
                'checkout_success', args=[booking.booking_number]))
        else:
            messages.error(request, 'There was an error with your booking.\
                Please double check your information and try again.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You haven't selected a product to rent!")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total_cost = current_bag['total_cost']
        rental_days = current_bag['rental_days']
        stripe_total = round(total_cost * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        booking_form = BookingForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, booking_number):
    """ Handle successful checkouts """
    booking = get_object_or_404(Booking, booking_number=booking_number)
    # product = get_object_or_404(Product, pk=product_id)
    # messages.success(request, f'Order successfully processed! \
    #     Your booking number is {booking_number}. A confirmation \
    #     email will be sent to {booking.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)
