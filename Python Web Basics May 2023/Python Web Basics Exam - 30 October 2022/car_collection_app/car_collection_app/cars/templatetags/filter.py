from django import template

register = template.Library()


@register.filter(name="price_filter")
def price_filter(price):
    return "%.3f" % price
