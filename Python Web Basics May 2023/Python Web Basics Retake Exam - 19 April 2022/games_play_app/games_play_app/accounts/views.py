from django.shortcuts import render

# Create your views here.


def create_profile(request):
    return render(request, "create-profile.html")


def profile_details(request):
    return render(request, "details-profile.html")


def edit_profile(request):
    return render(request, "edit-profile.html")


def delete_profile(request):
    return render(request, "delete-profile.html")
