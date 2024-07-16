
from django.db import models
from django.contrib.auth.models import User
from mod_ventas.sub_mod_productos.models import Producto


class Carrito(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    # def get_total_price(self):
    #     return self.cantidad * self.producto.precio