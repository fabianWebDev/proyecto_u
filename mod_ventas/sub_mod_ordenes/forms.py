from django import forms
from .models import Orden, OrdenItem

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields to be required
        for field in self.fields.values():
            field.required = True

class OrdenItemForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields = ['producto', 'cantidad']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields to be required
        for field in self.fields.values():
            field.required = True