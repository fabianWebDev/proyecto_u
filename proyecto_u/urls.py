"""
URL configuration for proyecto_u project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from proyecto_u import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('ventas/', include('mod_ventas.urls')),
    path('productos/', include('mod_ventas.sub_mod_productos.urls')),
    path('descuentos/', include('mod_ventas.sub_mod_descuentos.urls')),
    path('facturas/', include('mod_ventas.sub_mod_facturas.urls')),
    path('ordenes/', include('mod_ventas.sub_mod_ordenes.urls')),
    path('proveedores/', include('mod_ventas.sub_mod_proveedores.urls')),
    path('personas/', include('mod_personas.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', include('mod_login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
