from django.db import models

from users.models import BaseModel


class Notes(BaseModel):
    text = models.CharField(max_length=10000, verbose_name="Text")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="slug"
    )
    author = models.ForeignKey("users.User", on_delete=models.PROTECT)
    folders = models.ManyToManyField("api.Folder")

    def __str__(self):
        return self.slug


class Folder(BaseModel):
    name = models.CharField(max_length=50, verbose_name="name", unique=True)

    def __str__(self):
        return self.name
