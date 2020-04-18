from django.urls import path
from .views import  RegisterUsers, CustomTokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name="auth-register"),
    path('login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
