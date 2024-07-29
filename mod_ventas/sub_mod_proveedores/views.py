from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Proveedor
from .forms import ProveedorForm

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
    context_object_name= 'proveedores'
    
class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_detail.html'
    context_object_name = 'proveedor'
    
    # Optionally handle object not found scenario
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Proveedor.DoesNotExist:
            raise Http404("Proveedor not found")

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'sub_mod_proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'sub_mod_proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'sub_mod_proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')