from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm

# Create your views here.
def add_album(request):
    form = AlbumCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        
        return redirect('home')
    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context=context) 

def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context=context)

def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = AlbumEditForm(request.POST or None, instance=album)

    if form.is_valid():
        form.save()

        return redirect('home')
    
    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context=context)

def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = AlbumDeleteForm(request.POST or None, instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('home')
    
    context = {
        'album': album,
        'form': form,
    }


    return render(request, 'album/delete-album.html',context=context)
