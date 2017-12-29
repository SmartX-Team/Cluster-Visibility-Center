# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 04:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='created_at',
        ),
        migrations.AddField(
            model_name='api',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='api',
            name='desc',
            field=models.TextField(verbose_name='API 요약'),
        ),
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(max_length=100, verbose_name='API 명'),
        ),
        migrations.AlterField(
            model_name='api',
            name='url',
            field=models.URLField(verbose_name='API url'),
        ),
    ]
