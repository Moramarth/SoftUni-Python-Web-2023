from django.shortcuts import render

# Create your views here.


def profile_details(request):
    return render(request, "profile.html")


def edit_profile(request):
    return render(request, "edit-profile.html")


def delete_profile(request):
    return render(request, "delete-profile.html")
