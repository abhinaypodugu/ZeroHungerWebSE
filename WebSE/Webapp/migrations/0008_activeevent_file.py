# Generated by Django 3.1.2 on 2020-11-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0007_activeevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeevent',
            name='file',
            field=models.FileField(default='eventfiles/def.pdf', upload_to='eventfiles'),
        ),
    ]
