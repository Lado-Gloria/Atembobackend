
from temperature_recording.models import TemperatureHumidityRecord
from location.models import Location
from api.serializers import LocationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from flowrate.models import Device, FlowRate
from .serializers import DeviceSerializer, FlowRateSerializer, TemperatureHumidityRecordSerializer



class LocationListCreateView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceListAPIView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer= DeviceSerializer(devices, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer= DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




class DeviceDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            serializer = DeviceSerializer(device)
            return Response(serializer.data)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            serializer = DeviceSerializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            device.delete()
            return Response("Device successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class FlowrateListAPIView(APIView):
    def get(self, request):
        flows = FlowRate.objects.all()
        serializer= FlowRateSerializer(flows, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer= FlowRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 





class FlowrateDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            flow = FlowRate.objects.get(id=id)
            serializer = FlowRateSerializer(flow)
            return Response(serializer.data)
        except FlowRate.DoesNotExist:
            return Response("FlowRate not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TemperatureListView(APIView):
    serializer_class = TemperatureHumidityRecordSerializer
    def get_queryset(self):
        return TemperatureHumidityRecord.objects.all()
    def get(self, request):
        temperatures = self.get_queryset()
        serializer = TemperatureHumidityRecordSerializer(temperatures, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TemperatureHumidityRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TemperatureDetailView(APIView):
    serializer_class = TemperatureHumidityRecordSerializer
    def get_queryset(self):
        return TemperatureHumidityRecord.objects.all()
    def get_object(self, id):
        try:
            return self.get_queryset().get(id=id)
        except TemperatureHumidityRecord.DoesNotExist:
            raise Http404("Temperature not found")
    def get(self, request, id):
        temperature = self.get_object(id)
        serializer = TemperatureHumidityRecordSerializer(temperature)
        return Response(serializer.data)
    def put(self, request, id):
        temperature = self.get_object(id)
        serializer = TemperatureHumidityRecordSerializer(temperature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        temperature = self.get_object(id)
        temperature.delete()
        return Response("Temperature deleted", status=status.HTTP_204_NO_CONTENT)