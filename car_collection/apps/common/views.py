from django.shortcuts import render
from ..cars.models import Car

# Create your views here.
def index(request):
    
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all().order_by('pk')

    context = {
        'cars':cars
    }

    return render(request, 'common/catalogue.html', context=context)
