# Generated by Django 4.2.5 on 2023-10-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_remove_location_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='location',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]