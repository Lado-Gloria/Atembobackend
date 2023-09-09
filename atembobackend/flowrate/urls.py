from django.urls import path
from .views import WaterFlowList
app_name = 'flowrate'

urlpatterns = [
    path('flowrate/list', WaterFlowList, name='flowrate_list'),
]