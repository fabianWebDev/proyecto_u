from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Producto, TipoProducto
from .forms import ProductoForm, TipoProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'sub_mod_productos/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'sub_mod_productos/producto_detail.html'
    context_object_name = 'producto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Producto.DoesNotExist:
            raise Http404("Producto not found")

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'sub_mod_productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Producto creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el producto, intentelo nuevamente.')
        return super().form_invalid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'sub_mod_productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el producto, intentelo nuevamente.')
        return super().form_invalid(form)

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'sub_mod_productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Producto eliminado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al elimnar el producto, intentelo nuevamente.')
        return super().form_invalid(form)

    
class ProductoReportView(View):
    template_name = 'sub_mod_productos/producto_report.html'
    
    def get(self, request):
        productos = Producto.objects.all()
        total_stock = productos.aggregate(Sum('stock'))['stock__sum'] or 0
        total_precio_compra = productos.aggregate(Sum('precio_compra'))['precio_compra__sum'] or 0
        total_precio_venta = productos.aggregate(Sum('precio_venta'))['precio_venta__sum'] or 0
        
        context = {
            'productos': productos,
            'total_stock': total_stock,
            'total_precio_compra': total_precio_compra,
            'total_precio_venta': total_precio_venta,
        }
        return render(request, self.template_name, context)

class TipoProductoListView(ListView):
    model = TipoProducto
    template_name = 'sub_mod_productos/tipo_producto_list.html'
    context_object_name = 'tipos_productos'

class TipoProductoDetailView(DetailView):
    model = TipoProducto
    template_name = 'sub_mod_productos/tipo_producto_detail.html'
    context_object_name = 'tipo_producto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except TipoProducto.DoesNotExist:
            raise Http404("TipoProducto not found")

class TipoProductoCreateView(CreateView):
    model = TipoProducto
    form_class = TipoProductoForm
    template_name = 'sub_mod_productos/tipo_producto_form.html'
    success_url = reverse_lazy('tipo_producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de producto creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el tipo de producto, intentelo nuevamente.')
        return super().form_invalid(form)

class TipoProductoUpdateView(UpdateView):
    model = TipoProducto
    form_class = TipoProductoForm
    template_name = 'sub_mod_productos/tipo_producto_form.html'
    success_url = reverse_lazy('tipo_producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de producto actualizado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el tipo de producto, intentelo nuevamente.')
        return super().form_invalid(form)

class TipoProductoDeleteView(DeleteView):
    model = TipoProducto
    template_name = 'sub_mod_productos/tipo_producto_confirm_delete.html'
    success_url = reverse_lazy('tipo_producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de producto eliminado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al eliminar el tipo de producto, intentelo nuevamente.')
        return super().form_invalid(form)