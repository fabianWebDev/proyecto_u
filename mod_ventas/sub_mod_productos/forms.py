from django import forms
from .models import Producto
from mod_ventas.sub_mod_proveedores.models import Proveedor

class ProductoForm(forms.ModelForm):
    # Define the custom field outside of the Meta class
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select,
        label='Proveedor',
        empty_label=None  # Optional: removes the default empty label
    )

    class Meta:
        model = Producto
        fields = '__all__'