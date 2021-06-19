# Generated by Django 2.0.6 on 2018-08-10 16:16

from django.db import migrations, models
import site_config.models


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0003_auto_20171023_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='configfield',
            name='value_html',
            field=site_config.models.HTMLField(blank=True, null=True, verbose_name='HTML'),
        ),
        migrations.AlterField(
            model_name='configfield',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='configfield',
            name='splitter',
            field=models.CharField(blank=True, choices=[('newline', 'New line'), (',', 'Comma'), ('.', 'Dot'), (';', 'Semicolon'), (' ', 'Tab')], help_text='Доступно тільки для типів: text, input', max_length=10, null=True, verbose_name='Splitter'),
        ),
        migrations.AlterField(
            model_name='configfield',
            name='type',
            field=models.CharField(choices=[('input', 'Input'), ('text', 'Text'), ('html', 'HTML'), ('int', 'Integer'), ('float', 'Float'), ('bool', 'True / False'), ('url', 'Url'), ('email', 'Email'), ('file', 'File'), ('image', 'Image'), ('json', 'JSON')], max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='configfield',
            name='value_file',
            field=models.FileField(blank=True, null=True, upload_to='site_config', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='configfield',
            name='value_image',
            field=models.ImageField(blank=True, null=True, upload_to='site_config', verbose_name='Image'),
        ),
        migrations.AlterUniqueTogether(
            name='configfield',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='configfield',
            name='site',
        ),
    ]
