from django.contrib import admin
from django.urls import path, include
from .views import temperature_humidity_record_detail,create_temperature_humidity_record


urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature/',temperature_humidity_record_detail.as_View(),name="temperature_detail_view"),
    path('temperature/',create_temperature_humidity_record.as_View(),name="temperature_create_view")

]
