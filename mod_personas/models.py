from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido1 = models.CharField(max_length=100, default='')
    apellido2 = models.CharField(max_length=100, default='')
    correo_electronico = models.EmailField(default='')
    numero_telefonico = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido1} {self.apellido2}'

    def deactivate(self):
        self.activo = False
        self.save()

    def activate(self):
        self.activo = True
        self.save()

class Empleado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Empleado: {self.persona.nombre}'

class Cliente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f'Cliente: {self.persona.nombre}'
