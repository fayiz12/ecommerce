# Generated by Django 4.2.4 on 2023-08-20 04:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0003_rename_flag_image_path_countrymodel_flag_image_pat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="countrymodel",
            name="flag_image_pat",
        ),
    ]