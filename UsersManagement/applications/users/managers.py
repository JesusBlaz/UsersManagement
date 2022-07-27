from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models import Q

class UserManager(BaseUserManager, models.Manager):

    def __create_user(self, username, email, curp, rfc, password, is_staff, is_active, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            curp=curp,
            rfc=rfc,
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

    def create_superuser(self, username, email, curp, rfc, password=None, **extra_fields):
        return self.__create_user(username, email, curp, rfc, password, True, True, True, **extra_fields)

    def create_user(self, username, email, curp, rfc, password=None, **extra_fields):
        return self.__create_user(username, email, curp, rfc, password, False, True, False, **extra_fields)

    def list_by_keyword(self,user):
        """ Lista usuarios por palabra clave """

        return self.filter(
            Q(username__icontains=user) |
            Q(name__icontains=user) |
            Q(last_name__icontains=user)
        )
