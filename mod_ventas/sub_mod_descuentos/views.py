from django.shortcuts import render

# Create your views here.
def descuentos(request):
    crumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Ventas', 'url': '/ventas/'},
        {'name': 'Descuentos', 'url': '/descuentos/'},
    ]

    return render(request, 'sub_mod_descuentos/descuentos.html', {
        'crumbs': crumbs
    })
