# Generated by Django 4.2.4 on 2023-10-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_remove_orderitem_dicount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
