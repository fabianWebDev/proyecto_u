from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.core.exceptions import ValidationError

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(default='')
    numero_telefonico = models.IntegerField(default=0)
    tiempo_despacho_aprox = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    saldo_adeudado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    activo = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False)

    def get_absolute_url(self):
        return reverse("proveedor_detalle", args=[self.slug])
    
    def __str__(self):
        return self.nombre
    
    def clean(self):
        super().clean()
        if self.saldo_adeudado < 0:
            raise ValidationError({'saldo_adeudado': 'El saldo adeudado no puede ser menor a 0.'})
    
class PagoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pago de {self.cantidad} a {self.proveedor.nombre} en {self.fecha_pago}"
    
    def clean(self):
        super().clean()
        if self.saldo_adeudado < 0:
            raise ValidationError({'saldo_adeudado': 'El saldo adeudado no puede ser menor a 0.'})
        if self.cantidad < 0:
            raise ValidationError({'cantidad': 'La cantidad del pago no puede ser menor a 0.'})
        