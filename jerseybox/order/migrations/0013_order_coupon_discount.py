# Generated by Django 4.2.4 on 2023-10-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0012_review_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="coupon_discount",
            field=models.IntegerField(default=0),
        ),
    ]
