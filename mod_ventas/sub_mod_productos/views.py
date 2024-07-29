from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

# TODO: Add Breadcrumbs features
#     crumbs = [
#         {'name': 'Inicio', 'url': '/'},
#         {'name': 'Ventas', 'url': '/ventas/'},
#         {'name': 'Productos', 'url': '/productos/'},
#         {'name': producto.nombre , 'url': reverse('producto_detalle', args=[producto.slug])},
#     ]

class ProductoListView(ListView):
    model = Producto
    template_name = 'sub_mod_productos/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'sub_mod_productos/producto_detail.html'
    context_object_name = 'producto'

    # Optionally handle object not found scenario
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

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'sub_mod_productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'sub_mod_productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')