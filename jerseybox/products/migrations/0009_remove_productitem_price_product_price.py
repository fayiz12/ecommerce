# Generated by Django 4.2.4 on 2023-09-08 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_rename_actual_price_productitem_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productitem",
            name="price",
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
        ),
    ]
