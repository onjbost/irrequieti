from django.contrib import admin
from .models import *
# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ["name", "available", "top"]
    list_editable = ["available", "top"]

class TopStoryAdmin(admin.ModelAdmin):
    list_display =["story", "available"]
    list_editable = ["available"]

admin.site.register(Story, StoryAdmin)
admin.site.register(IpModel)
admin.site.register(LikeStory)
admin.site.register(TopStories, TopStoryAdmin)
