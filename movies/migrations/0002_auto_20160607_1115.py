# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 11:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='MovieImage',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=datetime.datetime(2016, 6, 7, 11, 15, 22, 308184, tzinfo=utc), upload_to='tmp/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.URLField(default=datetime.datetime(2016, 6, 7, 11, 15, 32, 68494, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
