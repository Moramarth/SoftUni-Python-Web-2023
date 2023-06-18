from django.shortcuts import render, redirect

from notes_app.accounts.models import Profile


# Create your views here.


def profile_details(request):
    user = Profile.objects.first()
    context = {"user": user}
    return render(request, "profile.html", context)


def delete_profile(request):
    user = Profile.objects.first()
    user.delete()
    return redirect('home_page')
