from django.shortcuts import render
from .models import *
# Create your views here.

def service_index(request):
    category = Category.objects.filter(available=True)
    context = {
        'category':category
    }
    return render(request, 'serviceindex.html', context)


def service_category(request, slug):
    category = Category.objects.get(slug=slug)
    service = Service.objects.filter(category=category, available=True)

    context = {
        'cat':category,
        'servs':service
    }

    if category.available == True:
        return render(request,'servicecategory.html', context)
    else:
        return render(request, '404.html')


def service(request, slug):
    service = Service.objects.get(slug=slug)
    context = {
        'service':service,
    }
    if service.available == True and service.category.available == True:
        return render(request, 'service.html', context)
    else:
        return render(request, '404.html')
