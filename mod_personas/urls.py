from django.urls import path
from .views import (
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
)

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona_list'),
    path('crear/', PersonaCreateView.as_view(), name='persona_crear'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona_detalle'),
    path('editar/<int:pk>/', PersonaUpdateView.as_view(), name='persona_editar'),
    path('borrar/<int:pk>/', PersonaDeleteView.as_view(), name='persona_borrar'),
]