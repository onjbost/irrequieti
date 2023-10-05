from django.urls import path, include
from .views import *


urlpatterns = [
    path('', service_index, name='service_index'),
    path('category/<slug:slug>/', service_category, name="service_cat"),
    path('service/<slug:slug>/', service, name="service")
]