# Generated by Django 5.2 on 2025-04-07 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdata', '0002_relative_relative_observations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relative',
            name='relative_observations',
        ),
    ]
