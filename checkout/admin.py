from django.contrib import admin
from .models import Booking, BookingLineItem


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)

    readonly_fields = ('booking_number', 'order_date', 'total_cost',)
    fields = ('booking_number', 'order_date', 'full_name',
                'email', 'phone_number', 'country',
                'postcode', 'town_or_city', 'street_address1',
                'street_address2', 'county', 'total_cost',
                'start_date')

    list_display = ('booking_number', 'order_date', 'full_name',
                    'total_cost',)

    ordering = ('-order_date',)


admin.site.register(Booking, BookingAdmin)
