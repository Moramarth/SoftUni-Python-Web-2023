from django.shortcuts import render

# Create your views here.


def create_car(request):
    return render(request, 'car-create.html')


def car_details(request, pk):
    return render(request, 'car-details.html')


def edit_car(request, pk):
    return render(request, 'car-edit.html')


def delete_car(request, pk):
    return render(request, 'car-delete.html')
