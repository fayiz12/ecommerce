# Generated by Django 4.2.4 on 2023-09-27 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_alter_address_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="phone_number",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="shipping_method",
            field=models.CharField(
                choices=[("standard", "Standard"), ("express", "Express")],
                default="standard",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="order.order",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("processing", "Processing"),
                    ("shipped", "Shipped"),
                    ("delivered", "Delivered"),
                ],
                default="processing",
                max_length=100,
            ),
        ),
    ]
