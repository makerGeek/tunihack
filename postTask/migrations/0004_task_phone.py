# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postTask', '0003_auto_20161127_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
