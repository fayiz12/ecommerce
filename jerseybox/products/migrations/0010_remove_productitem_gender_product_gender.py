# Generated by Django 4.2.4 on 2023-09-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_remove_productitem_price_product_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productitem",
            name="gender",
        ),
        migrations.AddField(
            model_name="product",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("kids", "Kids")],
                max_length=10,
                null=True,
            ),
        ),
    ]