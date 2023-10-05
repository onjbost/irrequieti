from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def attractionindex(request):
    attractions = Attraction.objects.filter(available=True)
    context = {
        'attrs':attractions,
        'seo_index':True,
    }
    return render(request, 'attractionindex.html', context)


def attraction(request, slug):
    attraction = Attraction.objects.get(slug=slug)
    context = {
        'attr':attraction,
        'seo_index':True,
    }

    if attraction.available==True:
        return render(request, 'attraction.html', context)
    else:
        return render(request, '404.html')
    
def like_attr(request, id):
    user = request.user
    attr_obj = Attraction.objects.get(id=id)
    if user in attr_obj.liked.all():
        attr_obj.liked.remove(user)
    else:
        attr_obj.liked.add(user)
        
    like, created = LikeAttraction.objects.get_or_create(user=user, attr=attr_obj)

    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect('attr', attr_obj.slug)