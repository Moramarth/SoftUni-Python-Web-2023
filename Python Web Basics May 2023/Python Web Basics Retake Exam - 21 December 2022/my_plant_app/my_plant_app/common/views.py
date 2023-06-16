from django.shortcuts import render

from my_plant_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    return render(request, template_name='home-page.html', context=context)


def display_catalogue(request):
    user = Profile.objects.first()
    plants = user.plant_set.all()
    context = {
        "user": user,
        "plants": plants,
    }
    return render(request, 'catalogue.html', context=context)
