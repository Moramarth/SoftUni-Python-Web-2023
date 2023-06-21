from django.shortcuts import render

from my_plant_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    return render(request, template_name='home-page.html')


def display_catalogue(request):
    return render(request, 'catalogue.html')
