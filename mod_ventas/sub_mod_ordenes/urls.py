from django.urls import path
from .views import (
    OrdenCreateView,
    OrdenDetailView,
    AgregarItemOrdenView,
    OrdenListView,
    ConfirmarCompletarOrdenView,
    OrdenReportView,
    SetTiempoDespachoView,
    OrdenesReportExportView,
    CancelarOrdenView
)

urlpatterns = [
    path('crear/', OrdenCreateView.as_view(), name='crear_orden'),
    path('<int:pk>/', OrdenDetailView.as_view(), name='detalle_orden'),
    path('<int:orden_id>/agregar_item/', AgregarItemOrdenView.as_view(), name='agregar_item_orden'),
    path('lista/', OrdenListView.as_view(), name='lista_ordenes'),
    path('<int:orden_id>/completar/', ConfirmarCompletarOrdenView.as_view(), name='completar_orden'),
    path('ordenes/report/', OrdenReportView.as_view(), name='orden_report'),
    path('<int:orden_id>/set_tiempo_despacho/', SetTiempoDespachoView.as_view(), name='set_tiempo_despacho'),
    path('ordenes/reporte/', OrdenesReportExportView.as_view(), name='ordenes_reporte_excel'),
    path('cancelar/<int:orden_id>/', CancelarOrdenView.as_view(), name='cancelar_orden'),
]