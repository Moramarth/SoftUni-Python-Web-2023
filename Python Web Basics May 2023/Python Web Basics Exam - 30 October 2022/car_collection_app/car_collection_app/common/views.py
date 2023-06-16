from django.shortcuts import render

from car_collection_app.accounts.models import ProfileModel


# Create your views here.


def home_page(request):
    user = ProfileModel.objects.first() or None
    context = {"user": user}
    return render(request, 'index.html', context=context)


def display_catalogue(request):
    user = ProfileModel.objects.first()

    context = {
        "user":  user,
    }
    
    return render(request, 'catalogue.html', context=context)
