## Terceros
from localflavor.mx.models import (
    MXCURPField,
    MXRFCField,
    MXZipCodeField,
)
from phonenumber_field.modelfields import PhoneNumberField

## Django
from django.db import models
# Gestión de usuarios
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """ Gestión de usuarios """

    GENDER_CHOICES = (
        ('M','MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO'),
    )

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)

    #
    curp = MXCURPField(blank=True)
    rfc = MXRFCField(blank=True)
    cp = MXZipCodeField(blank=True)
    phone_number = PhoneNumberField(region='MX',blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    # Instanciamos nuestro manager
    objects = UserManager()


    def __str__(self):
        return self.username
