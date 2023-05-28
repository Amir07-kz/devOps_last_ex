from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    UserManager as DjangoUserManager,
    PermissionsMixin,
)
from django.db import models

from users.enums import Role


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(email=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = "email"

    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    role = models.CharField(
        max_length=20, choices=Role.choices, verbose_name="Роль", default=Role.USER
    )
    telegram_user_id = models.PositiveIntegerField(
        verbose_name="Telegram user ID", null=True, blank=True
    )

    @property
    def is_staff(self):
        return self.role

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value
