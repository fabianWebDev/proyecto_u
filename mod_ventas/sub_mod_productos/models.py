from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date
from mod_ventas.sub_mod_proveedores.models import Proveedor

class TipoProducto(models.Model):
    nombre =  models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=1)
    precio_compra = models.FloatField(validators=[MinValueValidator(1)], default=0)
    precio_venta = models.FloatField(validators=[MinValueValidator(1)], default=0)
    codigo_lote = models.CharField(max_length=150, default='')
    stock = models.IntegerField(default=0)
    descuento = models.FloatField(default=0)
    fecha_vencimiento = models.DateField(default=date.today)
    slug = models.SlugField(default='', null=False)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre