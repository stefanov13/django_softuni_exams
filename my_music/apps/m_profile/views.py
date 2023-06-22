from django.shortcuts import render, redirect
from ..album.models import Album
from .models import Profile

# Create your views here.
def profile_details(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'profile/profile-details.html', context=context)


def profile_delete(request):
    albums = Album.objects.all()
    profile = Profile.objects.first()

    if request.method == 'POST':
        albums.delete()
        profile.delete()

        return redirect('home')

    return render(request, 'profile/profile-delete.html')
