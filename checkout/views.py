from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from products.models import Product
from .forms import BookingForm

import stripe


def checkout(request, product_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rental_days = int(request.POST.get('rentDays'))
    total_cost = int(product.price * rental_days)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=total_cost,
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
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'intent.client_secret'
    }

    return render(request, template, context)
