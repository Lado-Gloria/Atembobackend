from rest_framework import serializers
from location.models import Location



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Location
        fields = "__all__"

   
from flowrate.models import Device, FlowRate

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class FlowRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowRate
        fields = '__all__'
