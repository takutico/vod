# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160607_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(),
        ),
    ]
