from django.shortcuts import render, redirect

from my_music_app.accounts.forms import ProfileForm
from my_music_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}

    if user:
        return home_with_user(request, context)

    return home_no_user(request, context)


def home_with_user(request, context):
    return render(request, 'home-with-profile.html', context=context)


def home_no_user(request, context):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home page')
    context["form"] = form
    return render(request, 'home-no-profile.html', context=context)
