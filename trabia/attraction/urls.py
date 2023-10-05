from django.urls import path, include
from .views import *


urlpatterns = [
   path('', attractionindex, name='attr_index'),
   path('<slug:slug>/', attraction, name='attr'),
   path('like/attraction/<int:id>', like_attr, name='like_attr'),
]