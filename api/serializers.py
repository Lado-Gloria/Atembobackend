from pstats import Stats
from rest_framework import serializers
from rest_framework.response import Response

from temperature_recording.models import Device, TemperatureHumidityRecord




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



