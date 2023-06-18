from django.shortcuts import render, redirect

from online_library.accounts.forms import ProfileForm, ProfileDeleteForm
from online_library.accounts.models import Profile


# Create your views here.


def profile_details(request):
    user = Profile.objects.first()
    context = {"user": user}
    return render(request, "profile.html", context)


def edit_profile(request):
    user = Profile.objects.first()
    form = ProfileForm(initial=user.__dict__)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {"form": form}
    return render(request, "edit-profile.html", context)


def delete_profile(request):
    user = Profile.objects.first()
    form = ProfileDeleteForm(initial=user.__dict__, instance=user)
    if request.method == "POST":
        user.delete()
        return redirect('home page')
    context = {"form": form}
    return render(request, "delete-profile.html", context)
