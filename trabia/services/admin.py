from django.contrib import admin
from .models import *

# Register your models here.

class ServAdmin(admin.ModelAdmin):
    list_display = ["name", "category","available"]
    list_editable = ["available"]


class CatAdmin(admin.ModelAdmin):
    list_display = ["name", "available"]
    list_editable = ["available"]


admin.site.register(Service, ServAdmin)
admin.site.register(Category, CatAdmin)