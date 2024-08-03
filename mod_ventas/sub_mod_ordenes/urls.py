from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_orden, name='crear_orden'),
    path('<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('<int:orden_id>/agregar_item/', views.agregar_item_orden, name='agregar_item_orden'),
    path('lista/', views.lista_ordenes, name='lista_ordenes'),
    path('<int:orden_id>/completar/', views.completar_orden, name='completar_orden'),
]