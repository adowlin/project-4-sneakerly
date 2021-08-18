from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>', views.checkout, name='checkout'),
    path('checkout_success/<booking_number>', views.checkout_success, name='checkout_success'),
]
