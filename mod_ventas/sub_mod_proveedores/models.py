from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Proveedor(models.Model):
    nombre = models.CharField(max_length= 150)
    correo = models.EmailField(default='')
    numero_telefonico = models.IntegerField(default=0)
    tiempo_despacho_aprox = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    slug = models.SlugField(default='', null=False)
    activo = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("proveedor_detalle", args=[self.slug])
    
    def __str__(self):
        return self.nombre