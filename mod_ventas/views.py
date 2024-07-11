from django.shortcuts import render, get_object_or_404

def index(request):
    crumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Ventas', 'url': '/ventas/'},
    ]

    sub_mods_paths = [
        'productos',
        'descuentos',
        'facturas'
    ]
    
    return render(request, 'mod_ventas/index.html', {
        'crumbs': crumbs,
        'sub_mods_paths': sub_mods_paths
    })
