# Generated by Django 5.0.6 on 2024-05-18 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maitaxi', '0002_alter_trip_driver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='model_car',
            new_name='car',
        ),
    ]
