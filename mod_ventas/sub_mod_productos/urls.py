from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ProductoReportView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('borrar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_borrar'),
     path('productos/report/', ProductoReportView.as_view(), name='producto_report'),
]