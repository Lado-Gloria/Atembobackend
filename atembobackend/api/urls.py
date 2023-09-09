from django.urls import path
from .views import DeviceListAPIView, DeviceDetailView, FlowrateListAPIView, FlowrateDetailView

urlpatterns = [
    path('devices/', DeviceListAPIView.as_view(), name='device-list'),
    path('devices/<int:id>/', DeviceDetailView.as_view(), name='device-detail'),
    path('flowrate/', FlowrateListAPIView.as_view(), name='flowrate-list'),
    path('flowrate/<int:id>/', FlowrateDetailView.as_view(), name='flowrate-detail'),
]