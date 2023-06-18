from django.shortcuts import render, redirect
from .forms import ProfileCreateForm
from ..plant.models import Plant

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
    

    return render(request, 'plant_profile/profile-details.html')


def profile_edit(request):

    return render(request, 'plant_profile/edit-profile.html')


def profile_delete(request):

    return render(request, 'plant_profile/delete-profile.html')
