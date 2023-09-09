from django.urls import path
from .views import LocationListCreateView

urlpatterns = [
    path('api/locations/', LocationListCreateView.as_view(), name='location-list-create'),
]




