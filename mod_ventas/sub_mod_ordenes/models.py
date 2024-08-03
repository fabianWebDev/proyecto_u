from django.db import models
from django.contrib.auth.models import User
from mod_ventas.sub_mod_productos.models import Producto

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    direccion_envio = models.CharField(max_length=255)
    nombre_cliente = models.CharField(max_length=255, default='')
    numero_telefono_cliente = models.IntegerField(default=0)

    def __str__(self):
        return f'Orden {self.id} de {self.usuario.username}'

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'