from django.shortcuts import render, redirect

from online_library.accounts.forms import ProfileForm
from online_library.common.templatetags.tags import profile_status


# Create your views here.


def home_page(request):
    user = profile_status()
    if user:
        return home_page_with_user(request)
    return home_page_no_user(request)


def home_page_no_user(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    context = {"form": form}
    return render(request, "home-no-profile.html", context)


def home_page_with_user(request):
    return render(request, "home-with-profile.html")
