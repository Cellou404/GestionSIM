# Generated by Django 5.0.4 on 2024-05-10 10:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimCard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lot', models.CharField(db_default='Lot ?', max_length=10)),
                ('imsi', models.PositiveIntegerField(unique=True)),
                ('number', models.PositiveIntegerField(unique=True)),
                ('status', models.CharField(choices=[('ok', 'OK'), ('broken', 'BROKEN'), ('lost', 'LOST'), ('stolen', 'STOLEN')], default='ok', max_length=20)),
                ('in_stock', models.BooleanField(default=True, verbose_name='In stock')),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
