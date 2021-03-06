# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('geoLock', models.BooleanField(default=False)),
                ('language', models.CharField(max_length=20)),
                ('duration', models.IntegerField(default=0)),
                ('url', models.URLField()),
                ('format', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=movies.models.movie_image_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('publishedDate', models.DateTimeField()),
                ('availableDate', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParentalRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('scheme', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Type'),
        ),
        migrations.AddField(
            model_name='image',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='content',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]
