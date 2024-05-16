# Generated by Django 4.2.11 on 2024-05-15 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('experience', models.DecimalField(decimal_places=1, max_digits=3)),
                ('model_car', models.CharField(max_length=100)),
                ('car_id', models.CharField(max_length=6)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('col_review', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_point', models.CharField(max_length=255)),
                ('arrival_point', models.CharField(max_length=255)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maitaxi.driver')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
