import json

from rest_framework import (parsers, permissions, renderers, status, views, viewsets,)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from .permissions import IsOwnAccount

class UserViewSet(viewsets.ModelViewSet):
    """User API Views"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsOwnAccount(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'User could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """User login view"""

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():

            # Check if user has valid credentials and return user instance else None
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])

            if user is not None:

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                return Response({'msg':'Login successful', 'token': token, 'is_login_success': True}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'Credentials are not valid!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
