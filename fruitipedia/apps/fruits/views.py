from django.shortcuts import render, redirect
from .forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from .models import Fruit

# Create your views here.
def create_fruit(request):
    form = FruitCreateForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('dashboard')
    
    context = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context=context)


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context=context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)

    if form.is_valid():
        form.save()

        return redirect('dashboard')
    
    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/edit-fruit.html', context=context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        fruit.delete()

        return redirect('dashboard')
    
    context = {
        'form': form,
        'fruit': fruit,
    }
    
    return render(request, 'fruits/delete-fruit.html', context=context)
