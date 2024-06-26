# Generated by Django 5.0.2 on 2024-04-24 10:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="flavourpaan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("price", models.FloatField()),
                ("description", models.CharField(max_length=400)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("orders", models.CharField(max_length=100, null=True)),
                ("offers", models.CharField(default="", max_length=400, null=True)),
                ("benefit", models.CharField(default="", max_length=1000)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="paanaroma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("price", models.FloatField()),
                ("description", models.CharField(max_length=400)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("orders", models.CharField(max_length=100, null=True)),
                ("offers", models.CharField(default="", max_length=400, null=True)),
                ("benefit", models.CharField(default="", max_length=1000)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="specialpaan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("price", models.FloatField()),
                ("description", models.CharField(max_length=400)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("orders", models.CharField(max_length=100, null=True)),
                ("offers", models.CharField(default="", max_length=400, null=True)),
                ("benefit", models.CharField(default="", max_length=1000)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="sweetpaan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("price", models.FloatField()),
                ("description", models.CharField(max_length=400)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("orders", models.CharField(max_length=100, null=True)),
                ("offers", models.CharField(default="", max_length=400, null=True)),
                ("benefit", models.CharField(default="", max_length=1000)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=12)),
                ("address", models.CharField(max_length=1000)),
                ("address2", models.CharField(default="", max_length=1000)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=50)),
                ("zip", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("price", models.FloatField(default=0)),
                ("image", models.ImageField(default="", null=True, upload_to="")),
                ("quantity", models.IntegerField(default=0)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
