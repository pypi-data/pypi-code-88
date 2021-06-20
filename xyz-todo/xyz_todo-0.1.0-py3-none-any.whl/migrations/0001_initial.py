# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-27 11:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('target_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xbc\x96\xe5\x8f\xb7')),
                ('url', models.CharField(max_length=255, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
                ('is_done', models.BooleanField(default=False, verbose_name=b'\xe5\xb7\xb2\xe5\x8a\x9e')),
                ('expiration', models.DateTimeField(blank=True, default=datetime.datetime(2048, 8, 8, 0, 0), null=True, verbose_name=b'\xe8\xbf\x87\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('target_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType', verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='todos', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u5f85\u529e',
                'verbose_name_plural': '\u5f85\u529e',
            },
        ),
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together=set([('user', 'target_type', 'target_id', 'name')]),
        ),
    ]
