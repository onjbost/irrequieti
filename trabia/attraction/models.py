from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Attraction(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='attractions/', null=True)
    intro = models.TextField(default="", blank=None)
    description = RichTextField()
    available = models.BooleanField(default=True)
    top = models.BooleanField(default=False)
    location=models.CharField(max_length=1000)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)
    liked = models.ManyToManyField(User, default=None, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/attraction/%i/" % self.id
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def num_likes(self):
        return self.liked.all().count()

class TopAttraction(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.attraction.name
    

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)
    
class LikeAttraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attr = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)

    def __str__(self):
        return str(self.attr)