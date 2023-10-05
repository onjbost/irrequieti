from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *





urlpatterns = [
    path('', index, name='index'),
    path('chi_siamo/', about, name='about'),
    path('termini_e_condizioni/', terms, name='terms'),
    path('ads.txt/', Adview, name="ads"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
