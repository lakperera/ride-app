# Generated by Django 5.1 on 2024-09-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='is_createby',
            field=models.CharField(default=False),
        ),
        migrations.AddField(
            model_name='driver',
            name='is_updateby',
            field=models.CharField(default=False),
        ),
    ]
