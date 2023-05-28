from django.db import models


class Role(models.TextChoices):
    USER = "user", "Пользователь"
    ADMIN = "admin", "Администратор"
