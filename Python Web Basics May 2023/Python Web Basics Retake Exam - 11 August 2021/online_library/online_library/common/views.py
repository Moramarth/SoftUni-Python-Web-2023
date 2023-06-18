from django.shortcuts import render

from online_library.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    if user:
        return render(request, "home-with-profile.html", context)
    return render(request, "home-no-profile.html", context)
