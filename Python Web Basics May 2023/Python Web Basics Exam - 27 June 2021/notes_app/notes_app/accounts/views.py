from django.shortcuts import render, redirect

from notes_app.common.templatetags.tags import profile_status


# Create your views here.


def profile_details(request):
    return render(request, "profile.html")


def delete_profile(request):
    user = profile_status()
    user.delete()
    return redirect('home_page')
