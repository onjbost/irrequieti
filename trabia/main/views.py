from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from story.models import *
from services.models import *
from attraction.models import *
from communication.models import *

# Create your views here.

def index(request):

    ip=get_client_ip(request)
    main, create = Main.objects.get_or_create(id=1)
    
    if IpModel.objects.filter(ip=ip).exists():
        main.views.add(IpModel.objects.get(ip=ip))
        main.save()
    else:
        IpModel.objects.create(ip=ip)
        main.views.add(IpModel.objects.get(ip=ip))
    
    stories = Story.objects.filter(available=True, top=True)
    services = Category.objects.filter(available=True)
    attraction = Attraction.objects.filter(top=True)
    comunication = Comunication.objects.filter(available=True)

    

    context = {
        'home':True,
        'seo_index':True,
        'stories':stories,
        'services':services,
        'attractions':attraction,
        'comunications':comunication,
        'main':main,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'seo_index':True,
    }
    return render(request, 'about.html', context)

def terms(request):
    context = {
        'seo_index':False,
    }
    return render(request, 'terms.html', context)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip


def Adview(request):
    line =  """lijit.com, 476730, DIRECT, fafdf38b16bf6b2b #SOVRN
lijit.com, 476730-eb, DIRECT, fafdf38b16bf6b2b #SOVRN
openx.com, 538959099, RESELLER, 6a698e2ec38604c6
pubmatic.com, 137711, RESELLER, 5d62403b186f2ace
pubmatic.com, 156212, RESELLER, 5d62403b186f2ace
rubiconproject.com, 17960, RESELLER, 0bfd66d529a55807
appnexus.com, 1019, RESELLER, f5ab79cb980f11d1
video.unrulymedia.com, 12444764291, RESELLER
contextweb.com, 558511, RESELLER"""
    return HttpResponse(line, content_type="text/plain")
