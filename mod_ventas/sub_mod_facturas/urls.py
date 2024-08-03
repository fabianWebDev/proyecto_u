from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.facturas, name='facturas'),
    path('detalle/<int:pk>/', views.factura_detalle, name='factura_detalle'),
     path('monto-producto/', views.monto_facturado_por_producto, name='monto_facturado_por_producto'),
]
