from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home-page.html')


def display_dashboard(request):
    return render(request, 'dashboard.html')
