# Generated by Django 4.1.4 on 2023-01-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ADDRESS",
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
                ("uid", models.CharField(max_length=10)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("city", models.CharField(max_length=30)),
                ("land_mark", models.CharField(max_length=40)),
                ("district", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=30)),
                ("pin_code", models.DecimalField(decimal_places=0, max_digits=6)),
                ("phone", models.CharField(max_length=14)),
            ],
        ),
    ]
