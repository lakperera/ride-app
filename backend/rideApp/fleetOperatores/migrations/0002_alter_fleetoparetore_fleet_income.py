# Generated by Django 5.1 on 2024-08-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetOperatores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleetoparetore',
            name='fleet_income',
            field=models.IntegerField(null=True),
        ),
    ]
