from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Factura, FacturaDetalle
from django.db.models import Sum, F

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
        return FacturaDetalle.objects.values('producto').annotate(
            monto_total=Sum(F('cantidad') * F('precio_unitario'))
        ).order_by('producto')

    def handle_no_query_results(self):
        raise Http404("No FacturaDetalle found.")