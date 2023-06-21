from django import template

from online_library.accounts.models import Profile

register = template.Library()


@register.simple_tag()
def profile_status():
    return Profile.objects.first()
