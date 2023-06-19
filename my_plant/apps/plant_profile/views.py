from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, ProfileEditForm
from ..plant.models import Plant
from .models import Profile

# Create your views here.
def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('catalogue')
    
    context = {
        'form': form,
    }

    return render(request, 'plant_profile/create-profile.html', context=context)


def profile_details(request):
    plants = Plant.objects.all()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'plants': plants,

    }

    return render(request, 'plant_profile/profile-details.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')
    
    context = {
        'form': form,
    }

    return render(request, 'plant_profile/edit-profile.html', context=context)


def profile_delete(request):
    if request.method == 'POST':
        Plant.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('home-page')

    return render(request, 'plant_profile/delete-profile.html')
