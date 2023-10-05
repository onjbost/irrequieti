from django.urls import path, include
from .views import *


urlpatterns = [
    path('', story_index, name='story_index'),
    path('post/<slug:slug>/', story, name='story'),
    path('like/story/<int:id>', like_story, name='like_story'),
    path('views/add/<int:id>', add_visual, name='views_add'),
    path('tag/<slug:slug>', tagged, name="tagged"),
]