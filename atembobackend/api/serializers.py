from rest_framework import serializers
from location.models import Location
from flowrate.models import Device, FlowRate
from temperature_recording.models import TemperatureHumidityRecord 

class TemperatureHumidityRecordSerializer(serializers.ModelSerializer):
    humidity_with_unit = serializers.SerializerMethodField()
    temperature_with_unit = serializers.SerializerMethodField()

    class Meta:
        model = TemperatureHumidityRecord
        fields = ('id', 'device', 'time_stamp',  'humidity_with_unit', 'temperature_with_unit')

    def get_humidity_with_unit(self, obj):
        return f"{obj.humidity}% RH"

    def get_temperature_with_unit(self, obj):
        return f"{obj.temperature}°C"




class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Location
        fields = "__all__"

   

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class FlowRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowRate
        fields = '__all__'

