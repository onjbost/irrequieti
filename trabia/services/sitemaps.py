from django.contrib.sitemaps import Sitemap
from .models import *
from django.shortcuts  import reverse

class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Service.objects.filter(available=True)

class ServiceCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.filter(available=True)

class ServiceStaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['service_index']

    def location(self, item):
        return reverse(item)