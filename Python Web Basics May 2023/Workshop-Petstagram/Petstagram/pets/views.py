from django.shortcuts import render

from Petstagram.pets.models import Pet


# Create your views here.


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        "all_photos": all_photos,
        "pet": pet,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_name):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request, username, pet_name):
    return render(request, template_name='pets/pet-delete-page.html')
