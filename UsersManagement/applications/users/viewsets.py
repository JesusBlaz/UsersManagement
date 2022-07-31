from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
)
from .models import User



class UserViewSet(viewsets.ViewSet):
    """ ViewSet para la gestión de usuarios """

    queryset = User.objects.all()


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
            return Response(status=status.HTTP_200_OK,data=serializer.data)




