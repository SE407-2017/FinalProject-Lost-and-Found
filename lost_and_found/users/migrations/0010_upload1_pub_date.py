# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20171124_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload1',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
