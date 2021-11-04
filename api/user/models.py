from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # basic information
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class SuperAdmin(User):
    class Meta:
        proxy = True
        verbose_name = "Super Admin"
        verbose_name_plural = "Super Admins"


class Commoner(User):
    class Meta:
        proxy = True
        verbose_name = "Commoner"
        verbose_name_plural = "Commoners"