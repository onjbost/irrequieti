from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Service(models.Model):
    name = models.CharField(max_length=255)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField(null=True)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/service/%s/" % self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)