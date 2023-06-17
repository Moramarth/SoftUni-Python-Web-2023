from django.shortcuts import render

from my_music_app.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    if user:
        return render(request, 'home-with-profile.html', context=context)
    else:
        return render(request, 'home-no-profile.html', context=context)
