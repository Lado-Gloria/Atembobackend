from django.urls import path
from .views import LocationListCreateView
from .views import LocationDetailView

urlpatterns = [
    path('api/locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),

]




