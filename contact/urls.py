from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
]
