from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    # try:
        crumbs = [
            {'name': 'Inicio', 'url': '/'},
            {'name': 'Ventas', 'url': '/ventas/'},
        ]

        sub_mods_paths = [
            'producto_list',
            'descuentos',
            'facturas',
            'crear_orden',
            'proveedor_list'
        ]
        
        return render(request, 'mod_ventas/index.html', {
            'crumbs': crumbs,
            'sub_mods_paths': sub_mods_paths
        })
    # except NameError:
    #     return render(request, 'proyecto_u/404.html')
    # except Exception:
    #     return render(request, 'proyecto_u/404.html')
