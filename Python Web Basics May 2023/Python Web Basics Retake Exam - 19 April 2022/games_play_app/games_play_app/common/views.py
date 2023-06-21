from django.shortcuts import render

from games_play_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    return render(request, 'home-page.html')


def display_dashboard(request):
    return render(request, 'dashboard.html')
