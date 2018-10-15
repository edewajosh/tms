# Generated by Django 2.1.1 on 2018-10-15 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouApp', '0003_auto_20181015_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='published_on',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviced_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
