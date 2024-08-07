from django import forms
from .models import Proveedor, PagoProveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields to be required
        for field in self.fields.values():
            field.required = True
        
class PagoProveedorForm(forms.ModelForm):
    class Meta:
        model = PagoProveedor
        fields = ['proveedor', 'cantidad', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields to be required
        for field in self.fields.values():
            field.required = True
    
    def clean(self):
        cleaned_data = super().clean()
        numerical_fields = ['cantidad', 'precio_unitario']
        for field_name in numerical_fields:
            value = cleaned_data.get(field_name)
            if value is not None and value < 0:
                self.add_error(field_name, 'This field cannot be negative.')
        return cleaned_data