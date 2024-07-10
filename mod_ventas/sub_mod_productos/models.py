from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Producto(models.Model):
    nombre = models.CharField(max_length= 150)
    descripcion = models.TextField()
    precio = models.FloatField(validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("producto_detalle", args=[self.slug])