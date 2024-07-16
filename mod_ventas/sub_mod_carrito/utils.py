from .models import Carrito

def get_or_create_carrito(session):
    carrito_id = session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        session['carrito_id'] = carrito.id
    return carrito