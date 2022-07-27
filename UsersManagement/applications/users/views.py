## DRF
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
# Autenticación Rest
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
# Permissions Rest
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Serializers
from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserPagination,
)
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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        """ Creamos usuarios """

        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        rol_elegido = serializer.validated_data['rol']

        if rol_elegido == '1':
            # Creamos un superuser
            User.objects.create_superuser(
                serializer.validated_data['username'],
                serializer.validated_data['email'],
                serializer.validated_data['curp'],
                serializer.validated_data['rfc'],
                serializer.validated_data['password'],
                # Extra Fields
                name=serializer.validated_data['name'],
                last_name=serializer.validated_data['last_name'],
                gender=serializer.validated_data['gender'],
                cp=serializer.validated_data['cp'],
                phone_number=serializer.validated_data['phone_number'],
                date_of_birth=serializer.validated_data['date_of_birth'],
                rol=serializer.validated_data['rol']
            )
            return Response(
                {'mensaje': 'Administrador guardado con éxito'}
            )

        elif rol_elegido == '2' or rol_elegido == '3':
            # Creamos un user
            User.objects.create_user(
                serializer.validated_data['username'],
                serializer.validated_data['email'],
                serializer.validated_data['curp'],
                serializer.validated_data['rfc'],
                serializer.validated_data['password'],
                # Extra Fields
                name=serializer.validated_data['name'],
                last_name=serializer.validated_data['last_name'],
                gender=serializer.validated_data['gender'],
                cp=serializer.validated_data['cp'],
                phone_number=serializer.validated_data['phone_number'],
                date_of_birth=serializer.validated_data['date_of_birth'],
                rol=serializer.validated_data['rol']
            )
            return Response(
                {'mensaje': 'Usuario guardado con éxito'}
            )

        else:
            return Response(
                {'mensaje': 'Seleccione un rol, por favor.'}
            )


class UserListAPIView(ListAPIView):
    """ Api para listar los usuarios """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserListSerializer
    pagination_class = UserPagination

    def get_queryset(self):
        """ Mostramos los usuarios """

        buscar_user = self.request.query_params.get('usuario', '')
        return User.objects.list_by_keyword(buscar_user)


class UserRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    """ API que actualiza o elimina un usuario """
    pass





