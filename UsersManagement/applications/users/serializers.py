from rest_framework import serializers
# Models
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """ Serializador para crear usuarios """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'name',
            'last_name',
            'gender',
            'curp',
            'rfc',
            'cp',
            'phone_number',
            'date_of_birth',
            'rol',
        )


class UserListSerializer(serializers.ModelSerializer):
    """ Serializador para listar usuarios """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'gender',
            'curp',
            'rfc',
            'cp',
            'phone_number',
            'date_of_birth',
            'rol',
        )