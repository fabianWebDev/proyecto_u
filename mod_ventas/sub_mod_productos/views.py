from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.urls import reverse

def productos(request):
    crumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Ventas', 'url': '/ventas/'},
        {'name': 'Productos', 'url': '/productos'},
    ]

    productos = Producto.objects.all()
    
    return render(request, 'sub_mod_productos/productos.html', {
        'productos': productos,
        'crumbs': crumbs
    })

def producto_detalle(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    
    crumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Ventas', 'url': '/ventas/'},
        {'name': 'Productos', 'url': '/productos/'},
        {'name': producto.nombre , 'url': reverse('producto_detalle', args=[producto.slug])},
    ]
    
    return render(request, 'sub_mod_productos/producto_detalle.html', {
        'producto' : producto,
        'crumbs': crumbs
    })