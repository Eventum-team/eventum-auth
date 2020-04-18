from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import UntypedToken

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")

class CustomTokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()
    def validate(self, attrs):
        UntypedToken(attrs['token'])

        return "ok"
