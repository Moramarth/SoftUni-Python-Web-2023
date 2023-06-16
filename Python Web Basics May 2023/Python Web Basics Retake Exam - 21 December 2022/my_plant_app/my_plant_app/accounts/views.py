from django.shortcuts import render, redirect

from my_plant_app.accounts.forms import ProfileForm, ProfileEditForm
from my_plant_app.accounts.models import Profile


# Create your views here.


def create_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
        "user": None
        }
    return render(request, "create-profile.html", context=context)


def profile_details(request):
    user = Profile.objects.first()
    context = {"profile": user}
    return render(request, "profile-details.html", context=context)


def edit_profile(request):
    user = Profile.objects.first()
    form = ProfileEditForm(initial=user.__dict__, instance=user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile details")
    context = {"form": form}
    return render(request, "edit-profile.html", context=context)


def delete_profile(request):
    user = Profile.objects.first()
    if request.method == "POST":
        user.delete()
        return redirect('home page')

    return render(request, "delete-profile.html")
