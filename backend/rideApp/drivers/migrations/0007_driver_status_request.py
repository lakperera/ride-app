# Generated by Django 5.1 on 2024-08-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_driver_created_at_driver_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='status_request',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
