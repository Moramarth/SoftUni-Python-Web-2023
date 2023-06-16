from django.shortcuts import render

from games_play_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    return render(request, 'home-page.html', context=context)


def display_dashboard(request):
    user = Profile.objects.first()
    context = {"user": user}
    return render(request, 'dashboard.html', context=context)
