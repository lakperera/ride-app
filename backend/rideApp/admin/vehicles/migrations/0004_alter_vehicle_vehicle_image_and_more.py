# Generated by Django 5.1 on 2024-09-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_alter_vehicles_types_vehicle_types_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_image',
            field=models.FileField(null=True, upload_to='image/vehicles'),
        ),
        migrations.AlterField(
            model_name='vehicles_types',
            name='vehicle_custom_image',
            field=models.FileField(null=True, upload_to='image/vehicles_custom'),
        ),
    ]
