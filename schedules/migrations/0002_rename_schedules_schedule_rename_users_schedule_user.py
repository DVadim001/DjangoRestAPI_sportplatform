# Generated by Django 5.0.1 on 2024-04-27 09:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schedules',
            new_name='Schedule',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='users',
            new_name='user',
        ),
    ]
