# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_api_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='url',
            field=models.CharField(max_length=100, verbose_name='API url'),
        ),
    ]
