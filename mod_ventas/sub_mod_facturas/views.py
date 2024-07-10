from django.shortcuts import render

# Create your views here.
def facturas(request):
    return render(request, 'sub_mod_facturas/facturas.html')