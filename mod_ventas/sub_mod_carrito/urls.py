from django.urls import path
from . import views


urlpatterns = [
    path('', views.carrito, name="carrito"),
    path('agregar/<slug:slug>/', views.agregar, name='carrito_agregar'),
    path('eliminar/<slug:slug>/', views.eliminar, name='carrito_eliminar'),
]
