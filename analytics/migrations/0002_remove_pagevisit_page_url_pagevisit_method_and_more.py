# Generated by Django 5.0.1 on 2025-04-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagevisit',
            name='page_url',
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='method',
            field=models.CharField(default='GET', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='path',
            field=models.CharField(default='GET', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='user_agent',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='action_type',
            field=models.CharField(choices=[('registration', 'Registration'), ('event_signup', 'Event Signup'), ('event_create', 'Event Create'), ('content_interaction', 'Content Interaction')], max_length=50),
        ),
    ]
