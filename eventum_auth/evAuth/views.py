from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import EmailValidator
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_simplejwt.views import TokenViewBase
from django.core.exceptions import ValidationError
from .serializers import TokenSerializer, UserSerializer, CustomTokenVerifySerializer


def is_email(value):
    try:
        EmailValidator()(value)
    except ValidationError:
        return False
    else:
        return True

class CustomTokenVerifyView(TokenViewBase):
    serializer_class = CustomTokenVerifySerializer

class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):

        username = request.data.get("username", "")
        password = request.data.get("password", "")
        idUser = request.data.get("idUser", "")
        if User.objects.filter(username=username).exists():
                return Response(
                data={
                    "message": "user already exists"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not username or not password or not idUser:
            return Response(
                data={
                    "message": "incomplete form"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if is_email(username)==False:
            return Response(
                data={
                    "message": "not a valid email"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        new_user = User.objects.create_user(
            username=username, password=password, last_name=idUser
        )
        return Response(
            data={
                    "message": "user created"
                },
            status=status.HTTP_201_CREATED
        )
