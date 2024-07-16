from django.shortcuts import render, get_object_or_404, redirect
from mod_ventas.sub_mod_productos.models import Producto
from .models import Carrito, ItemCarrito
from .utils import get_or_create_carrito

# Create your views here.
def carrito(request):
    carrito = get_or_create_carrito(request.session)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    return render(request, 'sub_mod_carrito/carrito.html', {
        'carrito': carrito,
        'items_carrito': items_carrito
    })

def agregar(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    carrito = get_or_create_carrito(request.session)
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        item_carrito.cantidad += 1
    
    item_carrito.save()
    
    return redirect('carrito')

def eliminar(request, item_id):
    item_carrito = get_object_or_404(ItemCarrito, id=item_id)
    item_carrito.delete()

    return redirect('productos')
