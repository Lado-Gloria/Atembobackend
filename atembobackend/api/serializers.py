from rest_framework import serializers
from flowrate.models import Device, FlowRate

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class FlowRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowRate
        fields = '__all__'