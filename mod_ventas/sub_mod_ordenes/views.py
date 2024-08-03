# ordenes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Orden, OrdenItem
from .forms import OrdenForm, OrdenItemForm

@login_required
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.usuario = request.user
            orden.save()
            return redirect('detalle_orden', orden_id=orden.id)
    else:
        form = OrdenForm()
    return render(request, 'sub_mod_ordenes/crear_orden.html', {'form': form})

@login_required
def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    items = orden.items.all()
    return render(request, 'sub_mod_ordenes/detalle_orden.html', {'orden': orden, 'items': items})

@login_required
def agregar_item_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    if request.method == 'POST':
        form = OrdenItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.orden = orden
            item.save()
            return redirect('detalle_orden', orden_id=orden.id)
    else:
        form = OrdenItemForm()
    return render(request, 'sub_mod_ordenes/agregar_item_orden.html', {'form': form, 'orden': orden})

@login_required
def lista_ordenes(request):
    ordenes = Orden.objects.filter(usuario=request.user)
    return render(request, 'sub_mod_ordenes/ordenes_list.html', {'ordenes': ordenes})

@login_required
def completar_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    orden.completada = True
    orden.save()
    return redirect('detalle_orden', orden_id=orden.id)