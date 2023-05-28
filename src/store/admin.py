from django.contrib import admin

# Register your models here.
from store.models import Product, OrderInfo

admin.site.register(OrderInfo)
admin.site.register(Product)
