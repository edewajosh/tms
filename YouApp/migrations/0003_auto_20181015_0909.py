# Generated by Django 2.1.1 on 2018-10-15 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouApp', '0002_auto_20181011_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='serviced_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
