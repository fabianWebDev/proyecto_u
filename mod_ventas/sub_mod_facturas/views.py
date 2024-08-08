from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView
from django.views import View
from openpyxl import Workbook
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Factura, FacturaDetalle
from django.db.models import Sum, F
from mod_ventas.sub_mod_productos.models import Producto

class FacturaListView(LoginRequiredMixin, ListView):
    model = Factura
    template_name = 'sub_mod_facturas/facturas_list.html'
    context_object_name = 'facturas'
    paginate_by = 6

    def get_queryset(self):
        return Factura.objects.all()

    def handle_no_query_results(self):
        raise Http404("No Facturas found.")

class FacturaDetailView(LoginRequiredMixin, DetailView):
    model = Factura
    template_name = 'sub_mod_facturas/factura_detalle.html'
    context_object_name = 'factura'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Factura.DoesNotExist:
            raise Http404("Factura not found.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalles'] = FacturaDetalle.objects.filter(factura=self.object)
        return context

class MontoFacturadoPorProductoView(LoginRequiredMixin, ListView):
    template_name = 'sub_mod_facturas/monto_facturado_por_producto.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_queryset(self):
        return Producto.objects.annotate(
            monto_total=Sum(F('facturadetalle__cantidad') * F('facturadetalle__precio_unitario'))
        ).filter(facturadetalle__isnull=False).order_by('id')
        
    def handle_no_query_results(self):
        raise Http404("No FacturaDetalle found.")
    
class MontoFacturadoPorProductoExportView(View):
    def get(self, request):
        wb = Workbook()
        ws = wb.active
        ws.title = "Reporte de Productos Facturados"

        headers = [
            "ID Producto", "Nombre", "Tipo Producto", "Monto Total Facturado"
        ]
        ws.append(headers)

        productos = Producto.objects.annotate(
            monto_total=Sum(F('facturadetalle__cantidad') * F('facturadetalle__precio_unitario'))
        ).filter(facturadetalle__isnull=False).order_by('id')

        for producto in productos:
            row = [
                producto.id,
                producto.nombre,
                producto.tipo_producto.nombre if producto.tipo_producto else '',  # Asegúrate de convertir el objeto a un valor simple
                producto.monto_total or 0,
            ]
            ws.append(row)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=reporte_productos_facturados.xlsx'
        wb.save(response)

        return response