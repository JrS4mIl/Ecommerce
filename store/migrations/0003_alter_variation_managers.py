# Generated by Django 5.0.1 on 2024-01-25 16:25

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='variation',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
