from django.contrib import admin
from .models import *
# Register your models here.

class AttrAdmin(admin.ModelAdmin):
    list_display = ["name","available", "top"]
    list_editable = ["available", "top"]

class TopAttrAdmin(admin.ModelAdmin):
    list_display = ["attraction", "available"]
    list_editable  = ["available"]


admin.site.register(Attraction, AttrAdmin)
admin.site.register(TopAttraction, TopAttrAdmin)