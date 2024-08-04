from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Orden, OrdenItem
from .forms import OrdenForm, OrdenItemForm
from mod_ventas.sub_mod_facturas.models import Factura, FacturaDetalle
from django.db.models import Sum

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
    orden.tiempo_despacho_real = timezone.now()
    orden.save()
    
    total_orden = orden.get_total()
    
    factura = Factura.objects.create(
        total=total_orden
    )
    
    # Crear los detalles de la factura
    for item in orden.items.all():
        FacturaDetalle.objects.create(
            factura=factura,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.precio_unitario
        )
    
    # Asociar la factura a la orden
    orden.factura = factura
    orden.save()
    
    # Validar el tiempo de despacho
    if not orden.validar_tiempo_despacho():
        # Handle the case where the dispatch time is not valid
        # You can add a message or take some action
        pass
    
    return redirect('detalle_orden', orden_id=orden.id)

class OrdenReportView(View):
    template_name = 'sub_mod_ordenes/orden_report.html'
    
    def get(self, request):
        # Fetch all orders
        orders = Orden.objects.all()
        
        # Calculate totals
        total_orders = orders.count()
        total_items = OrdenItem.objects.aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        total_revenue = OrdenItem.objects.aggregate(Sum('precio_unitario'))['precio_unitario__sum'] or 0
        
        context = {
            'orders': orders,
            'total_orders': total_orders,
            'total_items': total_items,
            'total_revenue': total_revenue,
        }
        return render(request, self.template_name, context)