"""
URL configuration for trabia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import urls as main_urls
from services import urls as service_urls
from story import urls as story_urls
from communication import urls as comm_urls
from attraction import urls as attr_urls
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap


from story.sitemaps import StorySitemap, StoryStaticSitemap
from attraction.sitemaps import AttractionSitemap, AttractionStaticSitemap
from communication.sitemaps import CommunicationStaticSitemap
from services.sitemaps import ServiceStaticSitemap
from main.sitemaps import StaticViewSitemap


sitemaps = {

    'StorySitemap':StoryStaticSitemap,
    'TopStoriesSitemap': StorySitemap,

    'AttractionSitemap':AttractionStaticSitemap,
    'TopAttractionSitemap': AttractionSitemap,

    'CommunicationSitemap':CommunicationStaticSitemap,

    'ServiceSitemap':ServiceStaticSitemap,

    'MainSitemap': StaticViewSitemap
    }




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('story/', include(story_urls)),
    path('services/', include(service_urls)),
    path('attraction/', include(attr_urls)),
    path('communication/', include(comm_urls)),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


