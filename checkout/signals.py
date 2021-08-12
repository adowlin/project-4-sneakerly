from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookingLineItem


@receiver(post_save, sender=BookingLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Calculate booking total on lineitem update/create
    """
    instance.booking.calculate_total()


@receiver(post_delete, sender=BookingLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on linitem delete
    """
    instance.booking.calculate_total()
