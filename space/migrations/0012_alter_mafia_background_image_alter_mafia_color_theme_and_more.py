# Generated by Django 4.0.6 on 2022-07-25 04:17

import django.core.validators
from django.db import migrations, models
import utils.customfields


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0011_mafia_alter_rule_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mafia',
            name='background_image',
            field=utils.customfields.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='mafia_background/'),
        ),
        migrations.AlterField(
            model_name='mafia',
            name='color_theme',
            field=models.CharField(default='#00FFFFFF', max_length=16, validators=[django.core.validators.RegexValidator(code=400, message='not a valid hex color code', regex='^#+([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')]),
        ),
        migrations.AlterField(
            model_name='mafia',
            name='icon',
            field=utils.customfields.ContentTypeRestrictedFileField(blank=True, default='mafia-dashboards/loner-icon.svg', null=True, upload_to='mafia-dashboards/'),
        ),
    ]
