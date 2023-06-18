from django.shortcuts import render, redirect

from online_library.accounts.forms import ProfileForm
from online_library.accounts.models import Profile


# Create your views here.


def home_page(request):
    user = Profile.objects.first() or None
    context = {"user": user}
    if user:
        return home_page_with_user(request, context)
    return home_page_no_user(request, context)


def home_page_no_user(request, context):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    context["form"] = form
    return render(request, "home-no-profile.html", context)


def home_page_with_user(request, context):
    return render(request, "home-with-profile.html", context)
