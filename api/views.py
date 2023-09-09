from django.shortcuts import render

# Create your views here.
import statistics
from .serializers import TemperatureHumidityRecord, TemperatureHumidityRecordSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'PUT'])
def temperature_humidity_record_detail(request, pk):
    try:
        record = TemperatureHumidityRecord.objects.get(pk=pk)
    except TemperatureHumidityRecord.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TemperatureHumidityRecordSerializer(record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TemperatureHumidityRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=statistics.StatisticsError.HTTP_400_BAD_REQUEST)