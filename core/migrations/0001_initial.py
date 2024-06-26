# Generated by Django 5.0.4 on 2024-05-10 10:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plateforme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Platform Name')),
                ('description', models.TextField(blank=True, help_text='500 characters allowed.', max_length=500, null=True, verbose_name='Description of Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name of site')),
                ('address', models.CharField(max_length=100, verbose_name='Address of site')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='longitue')),
                ('altitude', models.PositiveSmallIntegerField(blank=True, help_text='Altitude in meters', null=True, verbose_name='longitue')),
            ],
        ),
    ]
