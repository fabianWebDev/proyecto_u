from django import forms
from .models import Orden, OrdenItem

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class OrdenItemForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields = ['producto', 'cantidad']