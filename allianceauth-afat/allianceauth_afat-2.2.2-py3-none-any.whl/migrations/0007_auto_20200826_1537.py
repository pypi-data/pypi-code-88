# Generated by Django 2.2.14 on 2020-08-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("afat", "0006_auto_20200820_2013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="afatlinktype",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
