from rest_framework import serializers, pagination
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
            'id',
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


class UserPagination(pagination.PageNumberPagination):
    """ Paginación para users """

    page_size = 5
    max_page_size = 50


class UserUpdateSerializer(serializers.ModelSerializer):
    """ Serializador para actualizar datos usuarios """

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
            'is_active',
        )