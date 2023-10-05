from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.


class Comunication(models.Model):
    name = models.CharField(max_length=255, null=True)
    subject = models.TextField()
    body = RichTextField()
    date = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return "/comunications/%i/" % self.id
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
