from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from registration.models import Registration
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class RegistrationListView(APIView):
    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegistrationDetailView(APIView):
    def get(self, request, id, format=None):
        registration = Registration.objects.get(id=id)
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        registration = Registration.objects.get(id=id)
        serializer = RegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        registration = Registration.objects.get(id=id)
        registration.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)