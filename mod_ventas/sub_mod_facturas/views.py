from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F
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
    
def monto_facturado_por_producto(request):
    productos = FacturaDetalle.objects.values('producto').annotate(
        monto_total=Sum(F('cantidad') * F('precio_unitario'))
    ).order_by('producto')

    return render(request, 'sub_mod_facturas/monto_facturado_por_producto.html', {
        'productos': productos,
    })