from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class AttractionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Attraction.objects.filter(available=True)

class AttractionStaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return  ['attr_index']

    def location(self, item):
        return reverse(item)