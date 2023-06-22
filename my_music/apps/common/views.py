from django.shortcuts import render,redirect
from ..m_profile.models import Profile
from ..m_profile.forms import ProfileCreateForm
from ..album.models import Album

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    albums = Album.objects.all().order_by('pk')
    form = ProfileCreateForm(request.POST or None)

    if profile:
        template = 'profile/home-with-profile.html'


    else:
        template = 'profile/home-no-profile.html'
        if form.is_valid():
            form.save()

            return redirect('home')
        

    context = {
        'form': form,
        'albums': albums,
    }
    

    return render(request, template_name=template, context=context)
