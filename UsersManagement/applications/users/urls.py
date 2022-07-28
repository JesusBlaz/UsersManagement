from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Views
from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'api/create-user/',
        views.UserCreateAPIView.as_view(),
        name='crear_user'
    ),
    path(
        'api/list-user/',
        views.UserListAPIView.as_view(),
        name='listar_user'
    ),
    path(
        'api/update-delete-user/<pk>/',
        views.UserRetrieveUpdateDestroyAPI.as_view(),
        name='update_delete_user'
    ),
    # Rest JWT Login
    path(
        'auth/login/',
        TokenObtainPairView.as_view(),
    ),
    path(
        'auth/token/refresh/',
        TokenRefreshView.as_view(),
    ),
]