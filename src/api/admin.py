from django.contrib import admin

# Register your models here.
from api.models import Folder, Notes

admin.site.register(Notes)
admin.site.register(Folder)
