from django.urls import path
from .views import RegistrationListView, RegistrationDetailView

urlpatterns = [
    path("registration/", RegistrationListView.as_view(), name="registration_list_view"),
    path("registration/<int:id>/", RegistrationDetailView.as_view(), name="registration_detail_view"),
]