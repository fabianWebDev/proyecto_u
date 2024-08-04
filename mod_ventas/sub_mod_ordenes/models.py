from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mod_ventas.sub_mod_facturas.models import Factura, FacturaDetalle
from mod_ventas.sub_mod_productos.models import Producto

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    direccion_envio = models.CharField(max_length=255)
    nombre_cliente = models.CharField(max_length=255, default='')
    numero_telefono_cliente = models.IntegerField(default=0)
    factura = models.OneToOneField(Factura, on_delete=models.SET_NULL, null=True, blank=True)
    tiempo_despacho_esperado = models.DateTimeField(default=timezone.now)
    tiempo_despacho_real = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Orden {self.id} de {self.usuario.username}'

    def get_total(self):
        return sum(item.get_total_price() for item in self.items.all())

    def validar_tiempo_despacho(self):
        if self.tiempo_despacho_real and self.tiempo_despacho_real > self.tiempo_despacho_esperado:
            return False
        return True

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.FloatField(default=0)

    def get_total_price(self):
        return self.cantidad * self.precio_unitario

    def save(self, *args, **kwargs):
        if self.producto:
            self.precio_unitario = self.producto.precio_venta
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto} - {self.cantidad} units"