# Generated by Django 3.1.2 on 2020-10-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0004_eventgallery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='date',
            field=models.DateTimeField(),
        ),
    ]