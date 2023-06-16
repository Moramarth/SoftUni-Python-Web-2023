from django import template

register = template.Library()


@register.filter(name="rating_format")
def rating_format(rating):
    return "%.1f" % rating
