from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return  [ "index", "about", "terms"]

    def location(self, item):
        return reverse(item)