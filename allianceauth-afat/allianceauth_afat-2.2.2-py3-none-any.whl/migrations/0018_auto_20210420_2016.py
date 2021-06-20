# Generated by Django 3.1.8 on 2021-04-20 20:16

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import afat.models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0014_auto_20210105_1413"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("afat", "0017_remove_soft_deletion"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aaafat",
            options={
                "default_permissions": (),
                "managed": False,
                "permissions": (
                    ("basic_access", "Can access the AFAT module"),
                    ("manage_afat", "Can manage the AFAT module"),
                    ("add_fatlink", "Can create FAT Links"),
                    ("stats_corporation_own", "Can see own corporation statistics"),
                    (
                        "stats_corporation_other",
                        "Can see statistics of other corporations",
                    ),
                    ("log_view", "Can view the modules log"),
                ),
                "verbose_name": "Alliance Auth AFAT",
            },
        ),
        migrations.AlterModelOptions(
            name="manualafat",
            options={
                "default_permissions": (),
                "verbose_name": "Manual FAT",
                "verbose_name_plural": "Manual FATs",
            },
        ),
        migrations.AddField(
            model_name="afatlink",
            name="reopened",
            field=models.BooleanField(
                default=False, help_text="Has this FAT link being re-opened?"
            ),
        ),
        migrations.AlterField(
            model_name="afat",
            name="afatlink",
            field=models.ForeignKey(
                help_text="The fatlink the character registered at",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="afat.afatlink",
            ),
        ),
        migrations.AlterField(
            model_name="afat",
            name="character",
            field=models.ForeignKey(
                help_text="Character who registered this fat",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="eveonline.evecharacter",
            ),
        ),
        migrations.AlterField(
            model_name="afatlink",
            name="character",
            field=models.ForeignKey(
                default=None,
                help_text="Character this fatlink has been created with",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="eveonline.evecharacter",
            ),
        ),
        migrations.AlterField(
            model_name="afatlink",
            name="creator",
            field=models.ForeignKey(
                help_text="Who created the fatlink?",
                on_delete=models.SET(afat.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="afatlink",
            name="link_type",
            field=models.ForeignKey(
                help_text="The fatlinks fleet type, if it's set",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="afat.afatlinktype",
            ),
        ),
        migrations.AlterField(
            model_name="manualafat",
            name="afatlink",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="afat.afatlink",
            ),
        ),
        migrations.AlterField(
            model_name="manualafat",
            name="character",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="eveonline.evecharacter",
            ),
        ),
        migrations.AlterField(
            model_name="manualafat",
            name="creator",
            field=models.ForeignKey(
                on_delete=models.SET(afat.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="AFatLog",
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
                ("log_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "log_event",
                    models.CharField(
                        choices=[
                            ("CR_FAT_LINK", "FAT Link Created"),
                            ("CH_FAT_LINK", "FAT Link Changed"),
                            ("RM_FAT_LINK", "FAT Link Removed"),
                            ("RO_FAT_LINK", "FAT Link Re-Opened"),
                            ("RM_FAT", "FAT Removed"),
                            ("CR_FAT_MAN", "Manual FAT Added"),
                        ],
                        default="CR_FAT_LINK",
                        max_length=11,
                    ),
                ),
                ("log_text", models.TextField()),
                ("fatlink_hash", models.CharField(max_length=254)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=models.SET(afat.models.get_sentinel_user),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "AFAT Log",
                "verbose_name_plural": "AFAT Logs",
                "default_permissions": (),
            },
        ),
    ]
