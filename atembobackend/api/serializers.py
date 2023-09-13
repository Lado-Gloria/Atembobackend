from rest_framework import serializers
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
