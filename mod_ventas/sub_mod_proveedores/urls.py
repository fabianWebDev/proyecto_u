from django.urls import path
from . import views


urlpatterns = [
    path('', views.proveedores, name='proveedores'),  
    path('<slug:slug>', views.proveedor_detalle, name='proveedor_detalle')
]
