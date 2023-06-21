from django.shortcuts import render, redirect

from my_music_app.accounts.models import Profile
from my_music_app.common.templatetags.tags import profile_status


# Create your views here.


def profile_details(request):
    return render(request, "profile-details.html")


def delete_profile(request):
    user = profile_status()
    if request.method == "POST":
        user.delete()
        return redirect("home page")
    return render(request, "profile-delete.html")
