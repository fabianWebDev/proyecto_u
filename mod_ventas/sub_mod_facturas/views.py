from django.shortcuts import render, get_object_or_404
from .models import Factura, FacturaDetalle

# Create your views here.
def facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'sub_mod_facturas/facturas.html', {
        'facturas': facturas,
    })
    
def factura_detalle(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = FacturaDetalle.objects.filter(factura=factura)
    return render(request, 'sub_mod_facturas/factura_detalle.html', {
        'factura': factura,
        'detalles': detalles,
    })