# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 07:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170815_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='author',
            field=models.CharField(default='Taekho Nam', max_length=10),
        ),
        migrations.AlterField(
            model_name='api',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='api',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='API description'),
        ),
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(max_length=20, verbose_name='API'),
        ),
    ]
