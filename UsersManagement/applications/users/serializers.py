## Terceros
from localflavor.mx.models import (
    MXCURPField,
    MXRFCField,
    MXZipCodeField,
)
from rest_framework import serializers
# Models
from .models import User


class UserCreateSerializer2(serializers.Serializer):
    """ Serializador para crear usuarios """

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    curp = serializers.CharField()
    rfc = serializers.CharField()
    cp = serializers.IntegerField()
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()
    rol = serializers.CharField()

class UserCreateSerializer(serializers.ModelSerializer):
    """ """

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