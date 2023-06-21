from django.shortcuts import render, redirect, get_object_or_404

from car_collection_app.cars.forms import CarCreateForm, CarDeleteForm
from car_collection_app.cars.models import CarModel
from car_collection_app.common.templatetags.tags import profile_data


# Create your views here.


def create_car(request):
    form = CarCreateForm()
    if request.method == "POST":
        user = profile_data()
        data = request.POST.copy()
        data["belongs_to"] = user.pk
        form = CarCreateForm(data)
        if form.is_valid():
            form.save()
            return redirect('display catalogue')
    context = {"form": form}
    return render(request, 'car-create.html', context=context)


def car_details(request, pk):
    car = get_object_or_404(CarModel, pk=pk)
    context = {"car": car}
    return render(request, 'car-details.html', context=context)


def edit_car(request, pk):
    car = get_object_or_404(CarModel, pk=pk)
    form = CarCreateForm(instance=car)
    if request.method == "POST":
        user = profile_data()
        data = request.POST.copy()
        data["belongs_to"] = user.pk
        form = CarCreateForm(data, instance=car)
        if form.is_valid():
            form.save()
            return redirect('display catalogue')
    context = {"form": form}
    return render(request, 'car-edit.html', context=context)


def delete_car(request, pk):
    car = get_object_or_404(CarModel, pk=pk)
    form = CarDeleteForm(instance=car)
    if request.method == "POST":
        car.delete()
        return redirect('display catalogue')
    context = {"form": form}
    return render(request, 'car-delete.html', context=context)
