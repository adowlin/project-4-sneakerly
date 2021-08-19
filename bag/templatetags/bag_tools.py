from django import template


register = template.Library()


@register.filter(name='calc_total')
def calc_total(price, rental_days):
    return price * rental_days
