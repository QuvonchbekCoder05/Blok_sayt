from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import AccessToken


class User (AbstractBaseUser, PermissionsMixin):
    """
    Moslashtirilgan User modeli.
    """
    email = models.EmailField(unique=True)  # Email unikal bo'lishi kerak
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False)  # Hisob faolligi
    is_staff = models.BooleanField(default=False)  # Admin saytga kirish uchun
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def generate_access_token(self):
        
        token = AccessToken.for_user(self)
        return str(token)
