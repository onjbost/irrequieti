from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class StorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Story.objects.filter(available=True)

class StoryStaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['story_index']

    def location(self, item):
        return reverse(item)

