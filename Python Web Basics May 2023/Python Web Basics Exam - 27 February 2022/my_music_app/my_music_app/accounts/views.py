from django.shortcuts import render, redirect

from my_music_app.accounts.models import Profile


# Create your views here.


def profile_details(request):
    user = Profile.objects.first()
    context = {"user": user}
    return render(request, "profile-details.html", context=context)


def delete_profile(request):
    user = Profile.objects.first()
    if request.method == "POST":
        user.delete()
        return redirect("home page")
    return render(request, "profile-delete.html")
