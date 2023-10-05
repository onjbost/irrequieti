from django.shortcuts import render
from .models import *
# Create your views here.

def comunicationindex(request):
    comunications = Comunication.objects.filter(available=True)
    context = {
        'comunications':comunications
    }
    return render(request, 'communicationindex.html', context)


def comunication(request, slug):
    comunication = Comunication.objects.get(slug=slug)
    context = {
        'comunication':comunication
    }
    if comunication.available == True:
        return render(request, 'communication.html', context)
    else:
        return render(request, '404.html')