# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_comments_xtd', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(unique_for_date='publish', verbose_name='slug')),
                ('body', models.TextField(verbose_name='body')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='publish')),
            ],
            options={
                'db_table': 'demo_articles',
                'ordering': ('-publish',),
            },
        ),

        migrations.CreateModel(
            name="Diary", 
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='body')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='publish')),
            ],
            options={
                'db_table': 'demo_diary',
                'ordering': ('-publish',),
            },            
        ),

        migrations.CreateModel(
            name='MyComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.XtdComment')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]
