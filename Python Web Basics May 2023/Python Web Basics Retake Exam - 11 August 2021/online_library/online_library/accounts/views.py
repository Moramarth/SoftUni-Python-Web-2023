from django.shortcuts import render, redirect

from online_library.accounts.forms import ProfileForm, ProfileDeleteForm
from online_library.common.templatetags.tags import profile_status


# Create your views here.


def profile_details(request):
    return render(request, "profile.html")


def edit_profile(request):
    user = profile_status()
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {"form": form}
    return render(request, "edit-profile.html", context)


def delete_profile(request):
    user = profile_status()
    form = ProfileDeleteForm(instance=user)
    if request.method == "POST":
        user.delete()
        return redirect('home page')
    context = {"form": form}
    return render(request, "delete-profile.html", context)
