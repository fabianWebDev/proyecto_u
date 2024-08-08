from django.urls import path
from .views import FacturaListView, FacturaDetailView, MontoFacturadoPorProductoView

urlpatterns = [
    path('', FacturaListView.as_view(), name='facturas'),
    path('factura/<int:pk>/', FacturaDetailView.as_view(), name='factura_detalle'),
    path('monto_facturado_por_producto/', MontoFacturadoPorProductoView.as_view(), name='monto_facturado_por_producto'),
]
