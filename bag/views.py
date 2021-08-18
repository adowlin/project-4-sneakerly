from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def bag(request, product_id):
    """ Add a product to the bag """
    bag = request.session.get('bag', {})

    product = get_object_or_404(Product, pk=product_id)
    start_date = request.POST.get('startDate')
    rental_days = int(request.POST.get('rentDays'))
    total_cost = int(product.price * rental_days)
    stripe_total = round(total_cost * 100)

    bag[start_date] = start_date
    bag[rental_days] = rental_days
    bag[total_cost] = total_cost
    bag[stripe_total] = stripe_total

    context = {
        'product': product,
        'start_date': start_date,
        'rental_days': rental_days,
        'total_cost': total_cost,
        'stripe_total': stripe_total,
    }

    request.session['bag'] = bag
    return render(request, 'bag/bag.html', context)


def remove_from_bag(request, product_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=product_id)

        bag = request.session.get('bag', {})

        bag.pop(product_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)