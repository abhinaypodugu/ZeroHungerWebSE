# Generated by Django 3.1.2 on 2020-10-31 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0005_auto_20201031_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]