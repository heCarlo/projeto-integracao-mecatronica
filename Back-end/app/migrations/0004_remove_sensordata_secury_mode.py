# Generated by Django 5.0 on 2023-12-09 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_securymode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='secury_mode',
        ),
    ]
