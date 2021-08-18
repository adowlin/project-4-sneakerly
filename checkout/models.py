import uuid

from django.db import models

from django_countries.fields import CountryField

from products.models import Product


class Booking(models.Model):
    booking_number = models.CharField(
        max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=False)
    rental_days = models.IntegerField(null=False, blank=False, default=0)
    product = models.CharField(
        max_length=500, null=False, blank=False, default='')
    product_size = models.CharField(
        max_length=4, null=False, blank=False, default='')
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def calculate_total(self):
        """
        Update grand total for each rental day.
        """
        self.total_cost = self.product_price * self.rental_days
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number


class BookingLineItem(models.Model):
    booking = models.ForeignKey(
        Booking, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=4, null=True, blank=True)
    rental_days = models.IntegerField(null=False, blank=False, default=0)
    booking_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking total
        and update the order total.
        """
        self.booking_total = self.product.price * self.rental_days
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on booking {self.booking.booking_number}'
