from django.urls import path
from . import views
from .views import OrdenReportView

urlpatterns = [
    path('crear/', views.crear_orden, name='crear_orden'),
    path('<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('<int:orden_id>/agregar_item/', views.agregar_item_orden, name='agregar_item_orden'),
    path('lista/', views.lista_ordenes, name='lista_ordenes'),
    path('<int:orden_id>/completar/', views.completar_orden, name='completar_orden'),
    path('orden/completar/confirmar/<int:orden_id>/', views.confirmar_completar_orden, name='confirmar_completar_orden'),
    path('ordenes/report/', OrdenReportView.as_view(), name='orden_report'),
    path('orden/tiempo_despacho/<int:orden_id>/', views.set_tiempo_despacho, name='set_tiempo_despacho'),
]