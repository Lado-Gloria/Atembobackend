from django.db import models

class Device(models.Model):
    serial_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default='Unknown')
class Meta:
    verbose_name_plural= "device"

class FlowRate(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    flow_rate = models.FloatField()

class Meta:
    verbose_name_plural = "flowrate"