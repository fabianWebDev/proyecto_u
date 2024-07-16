from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    try:
        crumbs = [
            {'name': 'Inicio', 'url': '/'},
            {'name': 'Ventas', 'url': '/ventas/'},
        ]

        sub_mods_paths = [
            'productos',
            'descuentos',
            'facturas',
            'ordenes',
            'proveedores'
        ]
        
        return render(request, 'mod_ventas/index.html', {
            'crumbs': crumbs,
            'sub_mods_paths': sub_mods_paths
        })
    except NameError:
        return render(request, 'proyecto_u/404.html')
    except Exception:
        return render(request, 'proyecto_u/404.html')
