# Generated by Django 4.2.4 on 2023-10-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0009_cart_coupon_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="coupon_discount",
            field=models.IntegerField(default=0),
        ),
    ]