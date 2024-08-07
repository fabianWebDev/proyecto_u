from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Sum

from .models import Orden, OrdenItem
from .forms import OrdenForm, OrdenItemForm
from mod_ventas.sub_mod_facturas.models import Factura, FacturaDetalle

class OrdenCreateView(LoginRequiredMixin, CreateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'sub_mod_ordenes/crear_orden.html'
    success_url = reverse_lazy('lista_ordenes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class OrdenDetailView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'sub_mod_ordenes/detalle_orden.html'
    context_object_name = 'orden'

    def get_queryset(self):
        return Orden.objects.filter(usuario=self.request.user)

class AgregarItemOrdenView(LoginRequiredMixin, FormView):
    form_class = OrdenItemForm
    template_name = 'sub_mod_ordenes/agregar_item_orden.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'orden': self.kwargs['orden_id']}
        return kwargs

    def form_valid(self, form):
        orden = get_object_or_404(Orden, id=self.kwargs['orden_id'], usuario=self.request.user)
        item = form.save(commit=False)
        item.orden = orden

        try:
            item.save()
            messages.success(self.request, 'Item added successfully.')
            return redirect('detalle_orden', pk=orden.id)
        except ValidationError as e:
            messages.error(self.request, e.message)
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = get_object_or_404(Orden, id=self.kwargs['orden_id'], usuario=self.request.user)
        return context

class OrdenListView(LoginRequiredMixin, ListView):
    model = Orden
    template_name = 'sub_mod_ordenes/ordenes_list.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        return Orden.objects.filter(usuario=self.request.user)

class ConfirmarCompletarOrdenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        orden_id = kwargs.get('orden_id')
        if not orden_id:
            messages.error(request, "Orden ID no proporcionado.")
            return redirect('lista_ordenes')

        try:
            orden = Orden.objects.get(pk=orden_id, usuario=request.user)
        except Orden.DoesNotExist:
            messages.error(request, "La orden no existe.")
            return redirect('lista_ordenes')

        return render(request, 'sub_mod_ordenes/completar_orden.html', {'orden': orden})

    def post(self, request, *args, **kwargs):
        orden_id = kwargs.get('orden_id')
        if not orden_id:
            messages.error(request, "Orden ID no proporcionado.")
            return redirect('lista_ordenes')

        try:
            orden = Orden.objects.get(pk=orden_id, usuario=request.user)
        except Orden.DoesNotExist:
            messages.error(request, "La orden no existe.")
            return redirect('lista_ordenes')

        if not orden.items.exists():
            messages.error(request, "La orden no tiene productos. No se puede completar.")
            return redirect('detalle_orden', pk=orden_id)

        orden.completada = True
        orden.save()

        total_orden = orden.get_total()
        factura = Factura.objects.create(total=total_orden)

        for item in orden.items.all():
            FacturaDetalle.objects.create(
                factura=factura,
                producto=item.producto,
                cantidad=item.cantidad,
                precio_unitario=item.precio_unitario
            )
            item.producto.stock -= item.cantidad
            item.producto.save()

        orden.factura = factura
        orden.save()

        if not orden.validar_tiempo_despacho():
            messages.warning(request, "El tiempo de despacho no es válido. Por favor, revisa los tiempos de entrega.")
            return redirect('detalle_orden', pk=orden_id)

        messages.success(request, "La orden ha sido completada y la factura generada correctamente.")
        return redirect('detalle_orden', pk=orden_id)

class OrdenReportView(LoginRequiredMixin, TemplateView):
    template_name = 'sub_mod_ordenes/orden_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Orden.objects.all()
        total_orders = orders.count()
        total_items = OrdenItem.objects.aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        total_revenue = OrdenItem.objects.aggregate(Sum('precio_unitario'))['precio_unitario__sum'] or 0

        context.update({
            'orders': orders,
            'total_orders': total_orders,
            'total_items': total_items,
            'total_revenue': total_revenue,
        })
        return context

class SetTiempoDespachoView(LoginRequiredMixin, UpdateView):
    model = Orden
    fields = ['tiempo_despacho_real']
    template_name = 'sub_mod_ordenes/set_tiempo_despacho.html'
    success_url = reverse_lazy('detalle_orden')

    def get_object(self):
        return get_object_or_404(Orden, id=self.kwargs['orden_id'], usuario=self.request.user)
