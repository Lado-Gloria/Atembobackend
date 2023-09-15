from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UserLoginView,TokenView

urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='farmer-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='farmer-retrieve-update-destroy'),
    path('login/', UserLoginView.as_view(), name='user-login'),
     path('token/', TokenView.as_view(), name='user-token'),
]