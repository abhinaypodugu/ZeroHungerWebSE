# Generated by Django 3.1.2 on 2020-10-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('des', models.CharField(max_length=256)),
            ],
        ),
    ]