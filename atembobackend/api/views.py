from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class TokenView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


