from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from django.contrib import messages

from .models import Proveedor, PagoProveedor
from .forms import ProveedorForm, PagoProveedorForm

# TODO: Add Breadcrumbs features
#     crumbs = [
#         {'name': 'Inicio', 'url': '/'},
#         {'name': 'Ventas', 'url': '/ventas/'},
#         {'name': 'Productos', 'url': '/productos/'},
#         {'name': producto.nombre , 'url': reverse('producto_detalle', args=[producto.slug])},
#     ]

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_detail.html'
    context_object_name = 'proveedor'

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'sub_mod_proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el proveedor, intentelo nuevamente.')
        return super().form_invalid(form)

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'sub_mod_proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el proveedor, intentelo nuevamente.')
        return super().form_invalid(form)

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor eliminado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al elimnar el proveedor, intentelo nuevamente.')
        return super().form_invalid(form)

class PagoProveedorListView(ListView):
    model = PagoProveedor
    template_name = 'sub_mod_proveedores/pago_list.html'
    context_object_name = 'pagos'

class PagoProveedorDetailView(DetailView):
    model = PagoProveedor
    template_name = 'sub_mod_proveedores/pago_detail.html'
    context_object_name = 'pago'

class PagoProveedorCreateView(CreateView):
    model = PagoProveedor
    form_class = PagoProveedorForm
    template_name = 'sub_mod_proveedores/pago_form.html'
    success_url = reverse_lazy('pago_list')

    def form_valid(self, form):
        messages.success(self.request, 'Pago registrado exitosamente!')
        proveedor = form.cleaned_data['proveedor']
        cantidad = form.cleaned_data['cantidad']
        proveedor.saldo_adeudado -= cantidad
        proveedor.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al registrar el pago, intentelo nuevamente.')
        return super().form_invalid(form)

class ProveedorReportView(View):
    template_name = 'sub_mod_proveedores/proveedor_report.html'
    
    def get(self, request):
        proveedores = Proveedor.objects.all()
        total_adeudado = proveedores.aggregate(Sum('saldo_adeudado'))['saldo_adeudado__sum'] or 0
        
        context = {
            'proveedores': proveedores,
            'total_adeudado': total_adeudado,
        }
        return render(request, self.template_name, context)