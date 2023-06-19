from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, ProfileEditForm
from .models import Profile

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

    return render(request, 'profile/profile-details.html')


def profile_edit(request):

    return render(request, 'profile/profile-edit.html')


def profile_delete(request):

    return render(request, 'profile/profile-delete.html')
