from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from .models import User


class UserSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='user-detail')
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'link', 'email', 'date_joined', 'is_staff',
                  'is_superuser', 'is_active', 'first_name', 'last_name',
                  'password',)
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        """Create the object"""
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    def validate(self, data):
        username = data.get('email',None)
        password = data['password']

        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise ValidationError("Invalid email/password.")

        # generate jwt token ??
        # data['token'] = generated jwt token??

        return data

