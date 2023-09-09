# Generated by Django 4.2.5 on 2023-09-09 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureHumidityRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_recording.device')),
            ],
        ),
    ]
