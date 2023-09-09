from rest_framework import serializers
from temperature_recording.models import  TemperatureHumidityRecord




class TemperatureHumidityRecordSerializer(serializers.Serializer):
    class Meta:
        model = TemperatureHumidityRecord
        fields ="__all__"



from rest_framework.response import Response
