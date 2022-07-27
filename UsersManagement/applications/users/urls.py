from django.urls import path
# Views
from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'api/create-user/',
        views.UserCreateAPIView.as_view(),
        name='crear_user'
    ),
]