from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'booking_history/<booking_number>',
        views.booking_history, name="booking_history"),
]
