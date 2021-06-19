# Generated by Django 2.2.1 on 2019-08-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('file', models.ImageField(max_length=255, upload_to='slider_images', verbose_name='File')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Slider image',
                'verbose_name_plural': 'Slider images',
                'ordering': ('order', 'id'),
            },
        ),
    ]
