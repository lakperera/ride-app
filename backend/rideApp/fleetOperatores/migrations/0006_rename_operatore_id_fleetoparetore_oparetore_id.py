# Generated by Django 5.1 on 2024-08-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fleetOperatores', '0005_remove_fleetoparetore_driver_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fleetoparetore',
            old_name='operatore_id',
            new_name='oparetore_id',
        ),
    ]
