# Generated by Django 4.0.6 on 2022-07-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration', '0008_alter_userevent_reguser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevent',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
