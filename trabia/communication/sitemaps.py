from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class CommunicationSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Comunication.objects.filter(available=True)

class CommunicationStaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['com_index']

    def location(self, item):
        return reverse(item)