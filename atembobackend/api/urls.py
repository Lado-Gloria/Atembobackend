from django.urls import path
from .views import DeviceListAPIView
from .views import FlowrateListAPIView


# app_name = 'api'

urlpatterns = [
    path('devices/', DeviceListAPIView.as_view(), name='device-list-create'),
    path('flowrate/', FlowrateListAPIView.as_view(), name='flowrate-list-create'),

]