from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .serializers import TokenSerializer, UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                # DRF JWT
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})

            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        username = email
        password = request.data.get("password", "")
        first_name = request.data.get("first_name", "")
        last_name= request.data.get("last_name", "")
        if not username and not password and not email:
            return Response(
                data={
                    "Mensaje": "Registro incorrecto"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )


class ListUserView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET users/:id/
    PUT users/:id/
    DELETE users/:id/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_user = self.queryset.get(pk=kwargs["pk"])
            return Response(UserSerializer(a_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    "message": "User with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            a_user = self.queryset.get(pk=kwargs["pk"])
            serializer = UserSerializer()
            updated_user = serializer.update(a_user, request.data)
            return Response(UserSerializer(updated_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    "message": "User with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            User.objects.get(pk=kwargs["pk"]).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(
                data={
                    "message": "User with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )



