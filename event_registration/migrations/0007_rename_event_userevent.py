# Generated by Django 4.0.6 on 2022-07-22 13:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_registration', '0006_rename_events_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='userEvent',
        ),
    ]
