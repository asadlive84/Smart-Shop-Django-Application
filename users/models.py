from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField("Phone Number", unique=True)
    objects = CustomUserManager()
