# Generated by Django 3.1.7 on 2021-03-27 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0011_auto_20210327_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='assign_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 13, 39, 17, 421357)),
        ),
        migrations.AlterField(
            model_name='courier',
            name='last_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 13, 39, 17, 421376)),
        ),
    ]
