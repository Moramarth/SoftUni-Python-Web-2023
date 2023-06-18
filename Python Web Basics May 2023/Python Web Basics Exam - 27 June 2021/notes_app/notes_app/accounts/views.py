from django.shortcuts import render

# Create your views here.


def profile_details(request):
    return render(request, "profile.html")
