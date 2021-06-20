# Generated by Django 3.1.1 on 2020-10-02 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("afat", "0009_auto_20200925_2206"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="afat",
            options={"verbose_name": "FAT", "verbose_name_plural": "FATs"},
        ),
        migrations.AlterModelOptions(
            name="afatdellog",
            options={
                "verbose_name": "Delete Log",
                "verbose_name_plural": "Delete Logs",
            },
        ),
        migrations.AlterModelOptions(
            name="afatlinktype",
            options={
                "verbose_name": "FAT Link Fleet Type",
                "verbose_name_plural": "FAT Link Fleet Types",
            },
        ),
        migrations.AlterModelOptions(
            name="clickafatduration",
            options={
                "verbose_name": "FAT Duration",
                "verbose_name_plural": "FAT Durations",
            },
        ),
        migrations.AlterModelOptions(
            name="manualafat",
            options={
                "verbose_name": "Manual FAT",
                "verbose_name_plural": "Manual FATs",
            },
        ),
    ]
