from pstats import Stats
import statistics
from rest_framework import serializers
from rest_framework.response import Response

from temperature.models import Device, TemperatureHumidityRecord


def temperature_humidity_record_detail(request, pk):
    try:
        record = TemperatureHumidityRecord.objects.get(pk=pk)
    except TemperatureHumidityRecord.DoesNotExist:
        return Response({"error": "Record does not exist"}, status=Stats.HTTP_404_NOT_FOUND)

    serializer = TemperatureHumidityRecordSerializer(record) 
    return Response(serializer.data, status=statistics.HTTP_200_OK)  

class TemperatureHumidityRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    time_stamp = serializers.DateTimeField(auto_now_add=True) 
    humidity = serializers.IntegerField()
    temperature = serializers.IntegerField()

    def create(self, validated_data):
        return TemperatureHumidityRecord.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.device = validated_data.get('device', instance.device)
        instance.time_stamp = validated_data.get('time_stamp', instance.time_stamp)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.save()
        return instance



