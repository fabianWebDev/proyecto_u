from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('<slug:slug>', views.producto_detalle, name='producto_detalle'),
]
