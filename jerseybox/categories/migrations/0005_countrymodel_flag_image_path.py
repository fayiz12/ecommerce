# Generated by Django 4.2.4 on 2023-08-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0004_remove_countrymodel_flag_image_pat"),
    ]

    operations = [
        migrations.AddField(
            model_name="countrymodel",
            name="flag_image_path",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
