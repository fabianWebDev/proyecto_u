from django.shortcuts import render

def index(request):
    return render(request, 'proyecto_u/index.html')