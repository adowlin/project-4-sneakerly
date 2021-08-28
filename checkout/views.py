from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Booking, BookingLineItem
from .forms import BookingForm
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment could not be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                booking_form = BookingForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                booking_form = BookingForm()
        else:
            booking_form = BookingForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'rental_days': rental_days,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, booking_number):
    """ Handle successful checkouts """
    booking = get_object_or_404(Booking, booking_number=booking_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        booking.user_profile = profile
        booking.save()

        profile_data = {
            'default_full_name': booking.full_name,
            'default_phone_number': booking.phone_number,
            'default_postcode': booking.postcode,
            'default_town_or_city': booking.town_or_city,
            'default_street_address1': booking.street_address1,
            'default_street_address2': booking.street_address2,
            'default_county': booking.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

        """Send the user a confirmation email"""
        cust_email = booking.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'booking': booking})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'booking': booking, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )  

    messages.success(request, f'Booking successfully processed! \
        Your booking number is {booking_number}. A confirmation \
        email will be sent to {booking.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)
