from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def __create_user(self, username, email, password, is_staff, is_active, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            **extra_fields
        )
        # Encriptamos el password
        user.set_password(password)
        # Guardamos el usario usando la misma base.
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self.__create_user(username, email, password, True, True, True, **extra_fields)

    def create_user(self, username, email, password=None, **extra_fields):
        return self.__create_user(username, email, password, False, True, False, **extra_fields)

