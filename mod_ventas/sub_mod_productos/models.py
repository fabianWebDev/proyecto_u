from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from datetime import date

class Producto(models.Model):
    # proveedor_id = models.CharField(max_length=255)
    # tipo_producto_id = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    # descuento = models.FloatField()
    precio_venta = models.FloatField(validators=[MinValueValidator(1)], default=0)
    precio_compra = models.FloatField(validators=[MinValueValidator(1)], default=0)
    codigo_lote = models.CharField(max_length=150, default='')
    fecha_vencimiento = models.DateField(default=date.today)
    activo = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("producto_detalle", args=[self.slug])

    def __str__(self):
        return self.nombre