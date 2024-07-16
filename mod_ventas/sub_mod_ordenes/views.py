from django.shortcuts import render

# Create your views here.
def ordenes(request):
    return render(request, 'sub_mod_ordenes/ordenes.html')