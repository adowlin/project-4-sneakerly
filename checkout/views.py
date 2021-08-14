from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .forms import BookingForm


def checkout(request, product_id):
    """ Rent a product for the specified number of days """

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rent_days = int(request.POST.get('rentDays'))
    total_price = product.price * rent_days

    if not rent_days:
        messages.error(request, "You haven't selected rental dates!")
        return redirect(reverse('products'))

    order_form = BookingForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'product': product,
        'start_date': start_date,
        'rent_days': rent_days,
        'total_price': total_price,
    }

    return render(request, template, context)
