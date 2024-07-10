from django.shortcuts import render, get_object_or_404

def index(request):
    
    crumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Ventas', 'url': '/ventas/'},
    ]
    
    return render(request, 'mod_ventas/index.html', {
        'crumbs':crumbs
    })
