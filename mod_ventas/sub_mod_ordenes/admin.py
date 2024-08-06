from django.contrib import admin
from .models import Orden, OrdenItem

# Register your models here.
admin.site.register(Orden)
admin.site.register(OrdenItem)