# Generated by Django 5.1 on 2024-08-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_alter_admin_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.CharField(default=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
