# Generated by Django 4.2.4 on 2023-09-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0006_address_name_address_phone_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_date",
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]