from django.contrib import admin
from django.urls import path, include
from .views import temperature_humidity_record_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature/',temperature_humidity_record_detail.as_View(),name="temperature_detail_view")
]
