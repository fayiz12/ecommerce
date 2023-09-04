# Generated by Django 4.2.4 on 2023-09-02 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_image_product_id_alter_product_club_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="image",
            name="product_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="products.productitem",
            ),
        ),
    ]