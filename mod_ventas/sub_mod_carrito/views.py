from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from mod_ventas.sub_mod_productos.models import Producto
from .models import Carrito, ItemCarrito
from .utils import get_or_create_carrito

def carrito(request):
    carrito = Carrito.objects.latest('id')
   
    if carrito is None:
        return HttpResponse("No carrito found for this user.")
    
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    precio_total = sum(item.get_total_price() for item in items_carrito)
    
    return render(request, 'sub_mod_carrito/carrito.html', {
        'carrito': carrito,
        'items_carrito': items_carrito,
        'precio_total': precio_total,
    })

def agregar(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    carrito = Carrito.objects.latest('id')
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        item_carrito.cantidad += 1
    
    item_carrito.save()
    return redirect('productos')

def eliminar(request, item_id):
    item_carrito = get_object_or_404(ItemCarrito, id=item_id)
    item_carrito.delete()

    return redirect('productos')
