from django import template

from car_collection_app.accounts.models import ProfileModel

register = template.Library()


@register.simple_tag()
def profile_data():
    return ProfileModel.objects.first()
