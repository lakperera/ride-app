# Generated by Django 5.1 on 2024-09-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('fleet_operators', '0002_fleetoparetore_is_createby_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FleetOparetore',
            new_name='FleetOperator',
        ),
    ]
