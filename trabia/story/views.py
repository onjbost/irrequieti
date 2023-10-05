from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from taggit.models import Tag
from django.core.paginator import Paginator

# Create your views here.


def story(request, slug):
    story = Story.objects.get(slug=slug)
    stories = Story.objects.prefetch_related('tag').all()
    context = {
            'seo_index':True,
            'story':story,
            'stories':stories
        }
    if story.available == True:
        return render(request, 'story.html', context)
    else:
        return render(request, '404.html')
    

    

def like_story(request, id):
    user = request.user
    story_obj = Story.objects.get(id=id)
    if user in story_obj.liked.all():
        story_obj.liked.remove(user)
    else:
        story_obj.liked.add(user)
        
    like, created = LikeStory.objects.get_or_create(user=user, story=story_obj)

    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect('story', story_obj.slug)

def story_index(request):
    stories = Story.objects.filter(available=True).order_by('-id')
    most_common = Story.tag.most_common()[:8]


    # Pagination
    p = Paginator(stories, 12)
    page = request.GET.get('page')
    story_page = p.get_page(page)
    nums = 'a' * story_page.paginator.num_pages

    context = {
        'seo_index':True,
        'stories':stories,
        'mc':most_common,
        'page':story_page,
        'nums':nums,
    }
    return render(request, 'storyindex.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Story.objects.filter(tag=tag)

    p = Paginator(posts, 12)
    page = request.GET.get('page')
    posts_page = p.get_page(page)
    nums = 'a' * posts_page.paginator.num_pages
    context = {
        'tag':tag,
        'stories': posts,
        'page': posts_page,
        'nums':nums,
    }
    return render(request, 'storyindex.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip


def add_visual(request, id):
    ip=get_client_ip(request)
    story = Story.objects.get(id=id)
    stories = Story.objects.prefetch_related('tag').all()
    print(ip)
    if IpModel.objects.filter(ip=ip).exists():
        story.views.add(IpModel.objects.get(ip=ip))
        story.save()
    else:
        IpModel.objects.create(ip=ip)
        story.views.add(IpModel.objects.get(ip=ip))

    return redirect('story', story.slug)
