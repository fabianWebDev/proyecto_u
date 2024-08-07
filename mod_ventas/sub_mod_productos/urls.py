from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ProductoReportView,
    TipoProductoListView,
    TipoProductoDetailView,
    TipoProductoCreateView,
    TipoProductoUpdateView,
    TipoProductoDeleteView,
    ProductoReportExportView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('borrar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_borrar'),
    path('productos/report/', ProductoReportView.as_view(), name='producto_report'),
    path('tipo-producto/', TipoProductoListView.as_view(), name='tipo_producto_list'),
    path('tipo-producto/<int:pk>/', TipoProductoDetailView.as_view(), name='tipo_producto_detail'),
    path('tipo-producto/crear/', TipoProductoCreateView.as_view(), name='tipo_producto_create'),
    path('tipo-producto/<int:pk>/editar/', TipoProductoUpdateView.as_view(), name='tipo_producto_update'),
    path('tipo-producto/<int:pk>/eliminar/', TipoProductoDeleteView.as_view(), name='tipo_producto_delete'),
    path('reporte/exportar/', ProductoReportExportView.as_view(), name='producto_report_export'),
]