from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total_cost = 0
    bag = request.session.get('bag', {})

    for product_id, rental_days in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total_cost = rental_days * product.price
        bag_items.append({
            'product_id': product_id,
            'rental_days': rental_days,
            'product': product,
            'total_cost': total_cost,
        })

    if bag_items:
        context = {
            'bag_items': bag_items,
            'total_cost': total_cost,
            'rental_days': rental_days,
        }
    else:
        context = {}

    return context
