from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nombre',)
    list_display = ('id', 'nombre', 'descripcion', 'precio_venta', 'precio_compra', 'stock', 'codigo_lote')

admin.site.register(Producto, ProductoAdmin)