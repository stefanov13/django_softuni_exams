from django.shortcuts import render, redirect
from .forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from .models import Plant

# Create your views here.
def plant_create(request):
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('catalogue')
    
    context = {
        'form': form
    }

    return render(request, 'plant/create-plant.html', context=context)


def plant_details(request, pk):
    crr_plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': crr_plant
    }

    return render(request, 'plant/plant-details.html', context=context)


def plant_edit(request, pk):
    crr_plant = Plant.objects.filter(pk=pk).get()
    form = PlantEditForm(request.POST or None, instance=crr_plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')


    context = {
        'plant': crr_plant,
        'form': form
    }

    return render(request, 'plant/edit-plant.html', context=context)


def plant_delete(request, pk):
    crr_plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=crr_plant)
    else:
        crr_plant.delete()
        return redirect('catalogue')


    context = {
        'plant': crr_plant,
        'form': form
    }
    return render(request, 'plant/delete-plant.html', context=context)
