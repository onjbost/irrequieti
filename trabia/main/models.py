from django.db import models
from story.models import IpModel

# Create your models here.

INITIAL_VIEWS = 6397


class Main(models.Model):
    views = models.ManyToManyField(IpModel, related_name='main_views', blank=True, editable=False, default=0)

    def total_views(self):
        return self.views.count() + INITIAL_VIEWS



