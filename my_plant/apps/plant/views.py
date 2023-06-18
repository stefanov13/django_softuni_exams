from django.shortcuts import render, redirect
from .forms import PlantCreateForm
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

    return render(request, 'plant/edit-plant.html')


def plant_delete(request, pk):

    return render(request, 'plant/delete-plat.html')
