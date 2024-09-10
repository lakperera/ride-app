# Generated by Django 5.1 on 2024-09-09 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0006_alter_ride_outbound_vehicle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='someone_else',
            name='ride',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='someone_else', to='dispatch.ride'),
            preserve_default=False,
        ),
    ]
