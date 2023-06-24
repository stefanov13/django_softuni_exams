from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, ProfileEditForm
from .models import Profile
from ..fruits.models import Fruit

# Create your views here.

def create_profile(request):
    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        
        return redirect('dashboard')
    
    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context=context)
    

def details_profile(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'profile/details-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()

        return redirect('details-profile')
    
    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    fruits = Fruit.objects.all()
    profile = Profile.objects.first()

    if request.method == 'POST':
        fruits.delete()
        profile.delete()

        return redirect('index')
    
    return render(request, 'profile/delete-profile.html')