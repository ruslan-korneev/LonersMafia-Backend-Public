# Generated by Django 4.0.6 on 2022-07-14 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_blacklistedip_datetime_blacklistedip_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_avatar',
            new_name='avatar',
        ),
    ]