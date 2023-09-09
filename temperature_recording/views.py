from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from .models import TemperatureHumidityRecord
# Register your models here.

class TemperaturehumidityAdmin(admin.ModelAdmin):
    list_temperature_humidity = ("device", "time_stamp", "humidity","temperature")
admin.site.register(TemperatureHumidityRecord ,TemperaturehumidityAdmin)