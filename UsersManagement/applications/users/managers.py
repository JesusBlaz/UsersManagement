from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def __create_user(self, username, email, curp, password, is_staff, is_active, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            curp=curp,
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

    def create_superuser(self, username, email, curp, password=None, **extra_fields):
        return self.__create_user(username, email, curp, password, True, True, True, **extra_fields)

    def create_user(self, username, email, curp, password=None, **extra_fields):
        return self.__create_user(username, email, curp, password, False, True, False, **extra_fields)

