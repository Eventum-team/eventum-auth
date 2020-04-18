from django.urls import path
from .views import  RegisterUsers, CustomTokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
