## DRF
from rest_framework.generics import (
    CreateAPIView,
)
# Serializers
from .serializers import UserCreateSerializer
# Response
from rest_framework.response import Response

## Django
from django.shortcuts import render
# Models
from .models import User


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    """ API para crear usuarios """

    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        """ Creamos usuarios """

        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(
            serializer.validated_data['username'],
            serializer.validated_data['email'],
            serializer.validated_data['password'],
            # Extra Fields
            name=serializer.validated_data['name'],
            last_name=serializer.validated_data['last_name'],
            gender=serializer.validated_data['gender'],
            curp=serializer.validated_data['curp'],
            rfc=serializer.validated_data['rfc'],
            cp=serializer.validated_data['cp'],
            phone_number=serializer.validated_data['phone_number'],
            date_of_birth=serializer.validated_data['date_of_birth'],
            rol=serializer.validated_data['rol'],
        )


        return Response(
            {'status': 'ok'}
        )







