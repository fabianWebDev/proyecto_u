from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') 
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': '',
            'password1': 'Ingrese una contraseña para su cuenta.',
            'password2': 'Ingrese la misma contraseña para verificar.',
        }
        error_messages = {
            'password_mismatch': 'Las contraseñas no coinciden.',
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )

    class Meta:
        fields = ('username', 'password')
        error_messages = {
            'invalid_login': 'Nombre de usuario o contraseña incorrectos.',
            'inactive': 'Esta cuenta está inactiva.',
        }