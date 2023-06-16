from django.shortcuts import render

# Create your views here.


def create_profile(request):
    return render(request, 'profile-create.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, "profile-delete.html")