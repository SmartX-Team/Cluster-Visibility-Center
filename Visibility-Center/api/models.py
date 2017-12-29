from django.db import models
from datetime import datetime

# Create your models here.
class API(models.Model):
    name = models.CharField(max_length=20, blank=False, verbose_name='API')
    desc = models.CharField(max_length=100, blank=False, verbose_name='API description')
    url = models.CharField(max_length=100, blank=False, verbose_name='API url',)
    date = models.DateField(default=datetime.now, verbose_name='Created at')
    author = models.CharField(max_length=10, blank=False, default='Taekho Nam')
