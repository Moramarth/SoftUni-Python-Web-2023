from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from .forms import PetForm, PetDeleteForm
from ..common.forms import CommentForm


# Create your views here.


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("show profile details", pk=1)
    context = {
        "form": form,
    }
    return render(request, template_name='pets/pet-add-page.html', context=context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm

    context = {
        "all_photos": all_photos,
        "pet": pet,
        "comment_form": comment_form,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username, pet_slug)
    context = {
        "form": form
    }
    return render(request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect("show profile details", pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        "form": form,
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
