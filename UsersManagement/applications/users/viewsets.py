from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# Permissions Rest
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsAdminIsRW

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserUpdateSerializer,
    ReadUserUpdateSerializer,
)
from .models import User


class UserViewSet(viewsets.ViewSet):
    """ ViewSet para la gestión de usuarios """

    def get_permissions(self):
        """ Definimos los permisos para las acciones y roles """

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsAdminIsRW]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    def list(self, request):
        """ Listamos usuarios por palabra clave """

        buscar_user = self.request.query_params.get('usuario', '')
        queryset = User.objects.list_by_keyword(buscar_user)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)

        if page is not None:
            serializer = UserListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = UserListSerializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        """ Creación de usuarios """

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

    def retrieve(self, request, pk=None):
        """ Recupera un usuario por pk """

        queryset = User.objects.get(id=pk)
        serializer = UserListSerializer(queryset)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """ Actualizamos usuario enviado por parámetro """

        instance = User.objects.get(id=pk)
        user = self.request.user
        if user.is_superuser or user.rol == 3:
            serializer = UserUpdateSerializer(instance, data=request.data, partial=True)
        else:
            serializer = ReadUserUpdateSerializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


