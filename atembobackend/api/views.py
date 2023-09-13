from .serializers import TemperatureHumidityRecord, TemperatureHumidityRecordSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 

@api_view(['GET', 'POST', 'PUT'])
def temperature_humidity_record_detail(request, pk):
    try:
        record = TemperatureHumidityRecord.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = TemperatureHumidityRecordSerializer(record)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TemperatureHumidityRecordSerializer(record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except TemperatureHumidityRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = TemperatureHumidityRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)