from django.contrib import admin
from .models import Carrito, ItemCarrito

# Register your models here.
admin.site.register(Carrito)
admin.site.register(ItemCarrito)