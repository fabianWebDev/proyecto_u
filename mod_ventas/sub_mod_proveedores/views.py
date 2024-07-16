from django.shortcuts import render, get_object_or_404
from .models import Proveedor

# Create your views here.
def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'sub_mod_proveedores/proveedores.html',{
        'proveedores': proveedores,
    })

def proveedor_detalle(request, slug):
    proveedor = get_object_or_404(Proveedor, slug=slug)
    return render(request, 'sub_mod_proveedores/proveedor_detalle.html', {
        'nombre': proveedor.nombre,
        'descripcion': proveedor.descripcion
    })