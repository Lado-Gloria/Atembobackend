from django import views
from django.urls import path

from .views import CustomUserDetailView, CustomUserListView, CustomUserLoginView


urlpatterns = [
    path('user/', CustomUserListView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail-view'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
]