from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Story(models.Model):
    name = models.CharField(max_length=255, default="helo")
    outline = RichTextField(null = True, blank=True)
    intro = models.TextField(null = True, blank=True)
    body = RichTextField(null = True, blank=True)
    img = models.ImageField(upload_to="images/", null = True, blank=True)
    fonti = RichTextField(null = True, blank=True)
    iframe = models.CharField(max_length=1000, null=True, blank=True)
    available = models.BooleanField(default=True)
    tag = TaggableManager()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)
    liked = models.ManyToManyField(User, default=None, blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    views = models.ManyToManyField(IpModel, related_name='post_views', blank=True, editable=False, default=0)
    top = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/story/post/{self.slug}/"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def total_views(self):
        return self.views.count()

    @property
    def num_likes(self):
        return self.liked.all().count()
    

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)
    
class LikeStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)

    def __str__(self):
        return str(self.story)
    



class TopStories(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.story.name

