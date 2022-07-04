"""
Serializers for the authentication API.

"""
from rest_framework import serializers
from .models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        read_only_fields = ['email']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone', 'customer', 'department']
        read_only_fields = ['id', 'email']

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def validate(self):
        super(UserRegisterSerializer, self).validate()

        return {
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    # def validate(self, data, *args, **kwargs):
    #     return super(UserRegisterSerializer, self).validate(data, *args, **kwargs)

