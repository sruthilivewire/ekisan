# Generated by Django 4.1.4 on 2023-02-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("KISAN_APP", "0002_alter_krishibhavan_ecode"),
    ]

    operations = [
        migrations.AddField(
            model_name="krishibhavan",
            name="uid",
            field=models.CharField(default="1", max_length=30),
            preserve_default=False,
        ),
    ]
