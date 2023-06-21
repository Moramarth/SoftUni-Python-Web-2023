from django.shortcuts import render, redirect

from my_music_app.accounts.forms import ProfileForm
from my_music_app.accounts.models import Profile
from my_music_app.common.templatetags.tags import profile_status


# Create your views here.


def home_page(request):
    user = profile_status()

    if user:
        return home_with_user(request)

    return home_no_user(request)


def home_with_user(request):
    return render(request, 'home-with-profile.html')


def home_no_user(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {"form": form}
    return render(request, 'home-no-profile.html', context=context)
