from django.shortcuts import render

def index(request):

    return render(request, 'common/home-page.html')


def catalogue(request):

    return render(request, 'common/catalogue.html')
