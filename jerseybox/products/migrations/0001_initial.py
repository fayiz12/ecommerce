# Generated by Django 4.2.4 on 2023-08-20 04:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "type",
                    models.CharField(
                        choices=[("away", "Away Jersey"), ("home", "Home Jersey")],
                        max_length=10,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("club", "Club"), ("country", "Country")],
                        max_length=10,
                    ),
                ),
                (
                    "club_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.club",
                    ),
                ),
                (
                    "country_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.countrymodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("stock", models.PositiveIntegerField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("kids", "Kids"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                        max_length=10,
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="image",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productitem",
                    ),
                ),
            ],
        ),
    ]
