# Generated by Django 4.0.6 on 2022-07-22 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0002_session_ended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 9, 8, 44, 582654)),
        ),
    ]
