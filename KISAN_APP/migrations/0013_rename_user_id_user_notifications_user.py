# Generated by Django 4.1.4 on 2023-02-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("KISAN_APP", "0012_rename_user_user_notifications_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_notifications", old_name="user_id", new_name="user",
        ),
    ]