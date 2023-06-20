from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, ProfileEditForm
from .models import Profile
from ..cars.models import Car

# Create your views here.
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    
    context = {
        'form':form
    }

    return render(request, 'profile/profile-create.html', context=context)


def profile_details(request):
    all_cars = Car.objects.all()

    total_price = sum(car.price for car in all_cars) 

    context = {
        'total_price': total_price,
    }

    return render(request, 'profile/profile-details.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')
    
    context = {
    #   'profile': profile,      This is not necessary because in template we have a profile from template-tag in base.html
        'form': form
    }

    return render(request, 'profile/profile-edit.html', context=context)


def profile_delete(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    if request.method == 'POST':
        cars.delete()
        profile.delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
