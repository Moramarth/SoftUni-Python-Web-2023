from django.shortcuts import render,redirect

from car_collection_app.accounts.forms import ProfileCreateForm


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
    return render(request, 'profile-details.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, "profile-delete.html")