from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .forms import BookingForm


def checkout(request, product_id):
    """ Rent a product for the specified number of days """

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rental_days = int(request.POST.get('rentDays'))
    total_cost = product.price * rental_days

    if not rental_days:
        messages.error(request, "You haven't selected rental dates!")
        return redirect(reverse('products'))

    booking_form = BookingForm()
    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'product': product,
        'start_date': start_date,
        'rental_days': rental_days,
        'total_cost': total_cost,
        'stripe_public_key': 'pk_test_51JORvtBQSuGyQwj4ISaaDySFXt4RhWUsFCpUP2hVa0PU8xsYg3PpMZrnzQxpABNij5W5r3PsRn2JQBQ8SHL4xE4D00CLngAK8z',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
