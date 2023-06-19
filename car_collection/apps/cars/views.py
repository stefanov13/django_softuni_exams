from django.shortcuts import render, redirect

# Create your views here.
def car_create(request):

    return render(request, 'car/car-create.html')


def car_details(request):

    return render(request, 'car/car-details.html')


def car_edit(request):

    return render(request, 'car/car-edit.html')


def car_delete(request):

    return render(request, 'car/car-delete.html')
