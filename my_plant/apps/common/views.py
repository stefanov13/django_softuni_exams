from django.shortcuts import render
from ..plant.models import Plant

def index(request):

    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }

    return render(request, 'common/catalogue.html', context=context)
