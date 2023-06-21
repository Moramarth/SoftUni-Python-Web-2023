from django.shortcuts import render, redirect, get_object_or_404

from my_plant_app.accounts.models import Profile
from my_plant_app.plants.forms import PlantForm, PlantDeleteForm
from my_plant_app.plants.models import Plant


# Create your views here.


def create_plant(request):
    form = PlantForm()
    if request.method == "POST":
        user = Profile.objects.first()
        data = request.POST.copy()
        data["belongs_to"] = user.pk
        form = PlantForm(data)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {"form": form}
    return render(request, 'create-plant.html', context=context)


def plant_details(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    context = {"plant": plant}
    return render(request, 'plant-details.html', context=context)


def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    form = PlantForm(instance=plant)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {"form": form}
    return render(request, 'edit-plant.html', context=context)


def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    form = PlantDeleteForm(instance=plant)
    if request.method == "POST":
        plant.delete()
        return redirect('catalogue')
    context = {"form": form}
    return render(request, 'delete-plant.html', context=context)
