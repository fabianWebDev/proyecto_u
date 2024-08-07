from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import Http404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from django.contrib import messages
from openpyxl import Workbook
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Proveedor, PagoProveedor
from .forms import ProveedorForm, PagoProveedorForm


class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_list.html'
    context_object_name = 'proveedores'
    paginate_by = 5

class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_detail.html'
    context_object_name = 'proveedor'

class ProveedorCreateView(LoginRequiredMixin, CreateView):
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

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
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

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor eliminado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al elimnar el proveedor, intentelo nuevamente.')
        return super().form_invalid(form)

class PagoProveedorListView(LoginRequiredMixin, ListView):
    model = PagoProveedor
    template_name = 'sub_mod_proveedores/pago_list.html'
    context_object_name = 'pagos'

class PagoProveedorDetailView(LoginRequiredMixin, DetailView):
    model = PagoProveedor
    template_name = 'sub_mod_proveedores/pago_detail.html'
    context_object_name = 'pago'

class PagoProveedorCreateView(LoginRequiredMixin, CreateView):
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

class ProveedorReportView(LoginRequiredMixin, View):
    template_name = 'sub_mod_proveedores/proveedor_report.html'
    
    def get(self, request):
        proveedores = Proveedor.objects.all()
        total_adeudado = proveedores.aggregate(Sum('saldo_adeudado'))['saldo_adeudado__sum'] or 0
        
        context = {
            'proveedores': proveedores,
            'total_adeudado': total_adeudado,
        }
        return render(request, self.template_name, context)
    
class ProveedorReportExportView(LoginRequiredMixin, View):
    def get(self, request):
        # Create a workbook and select the active worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Reporte de Proveedores"

        # Define the headers
        headers = [
            "ID Proveedor", "Nombre", "Correo", "Número Telefónico",
            "Tiempo Despacho"
        ]
        ws.append(headers)

        # Fetch data from the database
        proveedores = Proveedor.objects.all()

        # Write data to the worksheet
        for proveedor in proveedores:
            row = [
                proveedor.id,
                proveedor.nombre,
                proveedor.correo,
                proveedor.numero_telefonico,
                proveedor.tiempo_despacho_aprox,
            ]
            ws.append(row)

        # Create an HttpResponse object with the appropriate Excel header
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=reporte_proveedores.xlsx'

        # Save the workbook to the response
        wb.save(response)

        return response