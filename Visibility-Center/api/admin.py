from django.contrib import admin
from api.models import API

# Register your models here.
@admin.register(API)
class APIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'url', 'date', 'author']
