from django.urls import path
from .views import LoginView, RegisterUsers, ListUserView, UserDetailView


urlpatterns = [
    path('users/', ListUserView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user-details"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
]
