from django.urls import path
from .views import (
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
)

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor_list'),
    path('crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('<int:pk>/', ProveedorDetailView.as_view(), name='proveedor_detalle'),
    path('editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('borrar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_borrar'),
]