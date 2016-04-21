# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('book_info', models.TextField(max_length=1000)),
                ('book_year', models.IntegerField()),
                ('book_comments_count', models.IntegerField(default=0)),
                ('book_views_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_genre', models.CharField(max_length=100)),
                ('book', models.ManyToManyField(to='likeread.AboutBook')),
            ],
        ),
    ]
