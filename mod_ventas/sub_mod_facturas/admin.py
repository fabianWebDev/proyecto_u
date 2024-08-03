from django.contrib import admin
from .models import Factura, FacturaDetalle

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha_emision', 'total')

@admin.register(FacturaDetalle)
class FacturaDetalleAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio_unitario')