# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-10-25 09:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_auto_20200615_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pass', models.BooleanField(default=True, verbose_name='\u5df2\u901a\u8fc7')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passes', to='course.Course', verbose_name='\u8bfe\u7a0b')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passes', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u901a\u8fc7',
                'verbose_name_plural': '\u901a\u8fc7',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pass',
            unique_together=set([('course', 'user')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='pass',
            order_with_respect_to='course',
        ),
    ]
