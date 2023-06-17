from django.shortcuts import render

# Create your views here.


def profile_details(request):
    return render(request, "profile-details.html")


def delete_profile(request):
    return render(request, "profile-delete.html")
