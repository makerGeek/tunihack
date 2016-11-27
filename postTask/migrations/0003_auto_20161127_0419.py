# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postTask', '0002_auto_20161127_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='publishdate',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
