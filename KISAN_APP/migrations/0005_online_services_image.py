# Generated by Django 4.1.4 on 2023-02-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("KISAN_APP", "0004_online_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="online_services",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
