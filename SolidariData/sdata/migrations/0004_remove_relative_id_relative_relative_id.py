# Generated by Django 5.2 on 2025-04-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdata', '0003_remove_relative_relative_observations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relative',
            name='id',
        ),
        migrations.AddField(
            model_name='relative',
            name='relative_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
