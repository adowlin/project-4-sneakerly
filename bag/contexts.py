from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total_cost = 0

    context = {
        'bag_items': bag_items,
        'total_cost': total_cost,
    }

    return context
