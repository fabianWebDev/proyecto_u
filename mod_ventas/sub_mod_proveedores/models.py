from django.db import models
from django.urls import reverse

class Proveedor(models.Model):
    nombre = models.CharField(max_length= 150)
    descripcion = models.TextField()
    slug = models.SlugField(default='', null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("proveedor_detalle", args=[self.slug])