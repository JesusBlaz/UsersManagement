from rest_framework.permissions import BasePermission

class IsAdminIsRW(BasePermission):
    """ Permisos para admin y lectura/escritura """

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.rol == '3':
            return True

