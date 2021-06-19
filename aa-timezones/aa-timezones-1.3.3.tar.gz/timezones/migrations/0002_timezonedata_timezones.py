# Generated by Django 3.1.1 on 2020-09-27 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timezones", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimezoneData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timezone_name",
                    models.CharField(
                        help_text="Name of the timezone", max_length=255, unique=True
                    ),
                ),
                (
                    "utc_offset",
                    models.CharField(help_text="UTC of the timezone", max_length=255),
                ),
                (
                    "panel_id",
                    models.CharField(
                        help_text="ID of the timezone panel in frontend",
                        max_length=255,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Timezone Data",
                "verbose_name_plural": "Timezone Data",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Timezones",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "panel_name",
                    models.CharField(
                        help_text="Name of the timezone panel",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this timezone is enabled or not",
                    ),
                ),
                (
                    "timezone",
                    models.ForeignKey(
                        help_text="Selected timezone",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="timezones.timezonedata",
                    ),
                ),
            ],
            options={
                "verbose_name": "Timezone",
                "verbose_name_plural": "Timezones",
                "default_permissions": (),
            },
        ),
    ]
