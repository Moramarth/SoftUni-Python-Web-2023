from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from .forms import PetForm, PetDeleteForm
from ..accounts.models import PetstagramUser
from ..common.forms import CommentForm


# Create your views here.

@login_required
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect("show profile details", pk=request.user.pk)
    context = {
        "form": form,
    }
    return render(request, template_name='pets/pet-add-page.html', context=context)


@login_required
def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    owner = PetstagramUser.objects.get(username=username)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm

    context = {
        "all_photos": all_photos,
        "pet": pet,
        "comment_form": comment_form,
        "owner": owner,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


@login_required
def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', request.user.username, pet_slug)
    context = {
        "form": form
    }
    return render(request, template_name='pets/pet-edit-page.html', context=context)


@login_required
def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect("show profile details", request.user.username)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        "form": form,
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
