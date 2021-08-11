from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ View to show 'All Sneakers' page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_rental(request, product_id):
    """ View to show product rental booking page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_rental.html', context)
