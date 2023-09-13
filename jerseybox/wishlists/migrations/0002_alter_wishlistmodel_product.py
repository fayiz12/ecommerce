# Generated by Django 4.2.4 on 2023-09-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_remove_productitem_price_product_price"),
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlistmodel",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlist_item",
                to="products.product",
            ),
        ),
    ]
