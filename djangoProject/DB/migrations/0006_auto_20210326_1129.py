# Generated by Django 3.1.7 on 2021-03-26 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0005_auto_20210326_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='assign_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 11, 29, 54, 922966)),
        ),
        migrations.AlterField(
            model_name='courier',
            name='last_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 11, 29, 54, 922983)),
        ),
    ]
