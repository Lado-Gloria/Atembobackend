from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from flowrate.models import Device, FlowRate
from .serializers import DeviceSerializer, FlowRateSerializer


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
    def get(self, request,id, format=None):
        device= Device.objects.get(id=id)
        serializer=DeviceSerializer(device)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        device=Device.objects.get(id=id)
        serializer=DeviceSerializer(device,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        device=Device.objects.get(id=id)
        device.delete()
        return Response("device successfully deleted",status=status.HTTP_204_NO_CONTENT)    




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
    def get(self, request,id, format=None):
        flow= FlowRate.objects.get(id=id)
        serializer=DeviceSerializer(device)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        device=Device.objects.get(id=id)
        serializer=DeviceSerializer(device,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        device=Device.objects.get(id=id)
        device.delete()
        return Response("device successfully deleted",status=status.HTTP_204_NO_CONTENT)    



