from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TemperatureHumidityRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)  
    temperature = models.DecimalField(max_digits=5, decimal_places=2) 


    def __str__(self):
        return f"Device: {self.device.name}, Timestamp: {self.time_stamp}, Humidity: {self.humidity}%, Temperature: {self.temperature}°C"