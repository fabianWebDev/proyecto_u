from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date
from mod_ventas.sub_mod_productos.models import Producto

class Factura(models.Model):
    numero_factura = models.IntegerField(default=0)
    fecha_emision = models.DateField(default=date.today)
    total = models.FloatField(default=0)
    # Define related fields if needed
    # tipo_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_DEFAULT, default=1)
    # empleado = models.ForeignKey(Empleado, on_delete=models.SET_DEFAULT, default=1)
    # cliente = models.ForeignKey(Cliente, on_delete=models.SET_DEFAULT, default=1)
    # servicio_envio = models.ForeignKey(TipoServicio, on_delete=models.SET_DEFAULT, default=1)

    def get_absolute_url(self):
        return reverse("proveedor_detalle", args=[self.id])  # Adjust as needed

class FacturaDetalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Adjust as needed
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.producto} - {self.cantidad} units"