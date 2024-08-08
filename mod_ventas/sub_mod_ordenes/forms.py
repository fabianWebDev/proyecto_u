from django import forms
from .models import Orden, OrdenItem

#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     completada = models.BooleanField(default=False)
#     direccion_envio = models.CharField(max_length=255)
#     nombre_cliente = models.CharField(max_length=255, default='')
#     numero_telefono_cliente = models.IntegerField(default=0)
#     factura = models.OneToOneField(Factura, on_delete=models.SET_NULL, null=True, blank=True)
#     tiempo_despacho_esperado = models.DateTimeField(default=timezone.now)
#     tiempo_despacho_real = models.DateTimeField(null=True, blank=True)

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['usuario', 'direccion_envio', 'nombre_cliente', 'numero_telefono_cliente', 'tiempo_despacho_esperado']
        widgets = {
            'tiempo_despacho_esperado': forms.DateInput(attrs={'type': 'date'})
        }

class OrdenItemForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields = ['producto', 'cantidad']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields to be required
        for field in self.fields.values():
            field.required = True