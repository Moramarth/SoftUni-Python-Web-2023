from django.shortcuts import render, redirect

from car_collection_app.accounts.forms import ProfileCreateForm, ProfileEditForm
from car_collection_app.common.templatetags.tags import profile_data


# Create your views here.


def create_profile(request):
    form = ProfileCreateForm()
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display catalogue')
    context = {"form": form}
    return render(request, 'profile-create.html', context=context)


def profile_details(request):
    user = profile_data()
    total_car_price = sum([car.price for car in user.carmodel_set.all()])
    context = {
        "user": user,
        "total_car_price": total_car_price
    }
    return render(request, 'profile-details.html', context=context)


def edit_profile(request):
    user = profile_data()
    form = ProfileEditForm(instance=user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {"form": form}
    return render(request, 'profile-edit.html', context=context)


def delete_profile(request):
    user = profile_data()
    if request.method == "POST":
        user.delete()
        return redirect('home page')
    return render(request, "profile-delete.html")
