from django.urls import path

from .views import home_page, display_catalogue

urlpatterns = [
    path("", home_page, name='home page'),
    path("catalogue/", display_catalogue, name="catalogue"),
]