from django.shortcuts import render

# Create your views here.


def create_plant(request):
    return render(request, 'create-plant.html')


def display_catalogue(request):
    return render(request, 'catalogue.html')


def plant_details(request, pk):
    return render(request, 'plant-details.html')


def edit_plant(request, pk):
    return render(request, 'edit-plant.html')


def delete_plant(request, pk):
    return render(request, 'delete-plant.html')
