from django.contrib import admin
from .models import *
# Register your models here.


class ComAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "available"]
    list_editable = ["available"]

admin.site.register(Comunication, ComAdmin)