from django.urls import path
from . import views


urlpatterns = [
    path('', views.carrito, name="carrito"),
    path('agregar/<slug:slug>/', views.agregar, name='carrito_agregar'),
    path('eliminar/<int:id>/', views.eliminar, name='carrito_eliminar'),
]
