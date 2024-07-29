from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Persona
from .forms import PersonaForm

# TODO: Add Breadcrumbs features
#     crumbs = [
#         {'name': 'Inicio', 'url': '/'},
#         {'name': 'Ventas', 'url': '/ventas/'},
#         {'name': 'Productos', 'url': '/productos/'},
#         {'name': producto.nombre , 'url': reverse('producto_detalle', args=[producto.slug])},
#     ]

class PersonaListView(ListView):
    model = Persona
    template_name = 'mod_personas/persona_list.html'
    context_object_name = 'personas'

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'mod_personas/persona_detail.html'
    context_object_name = 'persona'

    # Optionally handle object not found scenario
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Persona.DoesNotExist:
            raise Http404("Persona not found")

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'mod_personas/persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'mod_personas/persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'mod_personas/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')