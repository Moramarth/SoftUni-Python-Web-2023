from django.shortcuts import render

from notes_app.accounts.models import Profile


# Create your views here.


def home_page_no_user(request, context):
    return render(request, "home-no-profile.html", context)


def home_page_with_user(request, context):
    return render(request, "home-with-profile.html", context)


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    if user:
        return home_page_with_user(request, context)
    return home_page_no_user(request, context)
