from django.urls import path
from .views import UserListView, UserDetailView, UserLoginView,UserRegistrationView

urlpatterns = [
    path("users/",UserListView.as_view(), name="registration_list_view"),
    path("user/<int:id>/", UserDetailView.as_view(), name="registration_detail_view"),
    path("register/", UserRegistrationView.as_view(), name="user_registration_view"),
    path("login/", UserLoginView.as_view(), name="user_login_view"), 
]