from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date
from django.core.exceptions import ValidationError
from mod_ventas.sub_mod_proveedores.models import Proveedor

class TipoProducto(models.Model):
    nombre =  models.CharField(max_length=100, default='')
    activo = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, default='productos/default.png')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=1)
    precio_compra = models.FloatField(validators=[MinValueValidator(1)], default=0)
    precio_venta = models.FloatField(validators=[MinValueValidator(1)], default=0)
    codigo_lote = models.CharField(max_length=150, default='')
    stock = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(default=date.today)
    slug = models.SlugField(default='', null=False)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    def clean(self):
        super().clean()
        if self.fecha_vencimiento < date.today():
            raise ValidationError({'fecha_vencimiento': 'La fecha de vencimiento no puede ser menor a la fecha actual.'})
        if self.precio_compra < 0:
            raise ValidationError({'precio_compra': 'El precio de compra no puede ser menor a 0.'})
        if self.precio_venta < 0:
            raise ValidationError({'precio_venta': 'El precio de venta no puede ser menor a 0.'})
        if self.stock < 0:
            raise ValidationError({'stock': 'El stock no puede ser menor a 0.'})