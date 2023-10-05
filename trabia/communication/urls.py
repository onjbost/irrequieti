from django.urls import path, include
from .views import *


urlpatterns = [
   path('', comunicationindex, name='com_index'),
   path('<slug:slug>/', comunication, name='com')
]