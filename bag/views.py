from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def bag(request, product_id):
    """ Add a product to the bag """
    bag = request.session.get('bag', {})
    """
    If a product is already in the bag, clear it.
    Only 1 product can be rented at one time.
    """
    if bag:
        bag.clear()

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rental_days = int(request.POST.get('rentDays'))
    total_cost = int(product.price * rental_days)
    stripe_total = round(total_cost * 100)

    bag[product_id] = rental_days

    context = {
        'product': product,
        'start_date': start_date,
        'rental_days': rental_days,
        'total_cost': total_cost,
        'stripe_total': stripe_total,
    }

    request.session['bag'] = bag
    return render(request, 'bag/bag.html', context)
