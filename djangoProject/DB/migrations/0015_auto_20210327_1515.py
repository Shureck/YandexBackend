# Generated by Django 3.1.7 on 2021-03-27 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0014_auto_20210327_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='assign_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 15, 15, 53, 477198)),
        ),
        migrations.AlterField(
            model_name='courier',
            name='last_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 15, 15, 53, 477219)),
        ),
    ]
