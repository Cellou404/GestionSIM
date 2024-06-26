# Generated by Django 5.0.4 on 2024-05-10 10:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lot', models.CharField(db_default='Lot ?', max_length=10)),
                ('imsi', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('device_type', models.CharField(blank=True, max_length=150, null=True)),
                ('imei', models.CharField(max_length=16, unique=True)),
                ('registration_number', models.CharField(max_length=50, verbose_name='registration number')),
                ('asset_description', models.CharField(max_length=50, verbose_name='asset description')),
                ('site', models.CharField(blank=True, max_length=200, null=True)),
                ('plateforme', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
                'ordering': ['imei'],
            },
        ),
        migrations.CreateModel(
            name='MobileDeviceType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code_name', models.CharField(help_text='e.g: fmb140', max_length=20, verbose_name='code name')),
                ('device_name', models.CharField(help_text='e.g: Teltonika FMB140', max_length=50, verbose_name='device name')),
                ('description', models.TextField(blank=True, help_text='500 characters allowed', max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Mobile Device Type',
                'verbose_name_plural': 'Mobile Device Types',
            },
        ),
    ]
