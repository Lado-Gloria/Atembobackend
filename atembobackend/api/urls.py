from django.urls import URLPattern, path
from .views import TemperatureListView, TemperatureDetailView  # Import your Temperature views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings



schema_view = get_schema_view(
    openapi.Info(
      title="temperature_recording",
      default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path("Temperature/", TemperatureListView.as_view(), name="temperature_list_view"),
    path("Temperature/<int:id>/", TemperatureDetailView.as_view(), name="temperature_detail_view"),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
