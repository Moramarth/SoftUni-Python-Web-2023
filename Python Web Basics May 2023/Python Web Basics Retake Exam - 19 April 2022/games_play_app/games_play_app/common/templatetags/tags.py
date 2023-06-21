from django import template

from games_play_app.accounts.models import Profile

register = template.Library()


@register.simple_tag()
def profile_status():
    return Profile.objects.first()
