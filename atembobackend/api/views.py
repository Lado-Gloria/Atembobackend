from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from temperature_recording.models import TemperatureHumidityRecord
from .serializers import TemperatureHumidityRecordSerializer
from django.http import Http404

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
