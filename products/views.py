from django.shortcuts import render
from .models import Product


def all_products(request):
    """ View to return 'All Sneakers' page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
