from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.error(request, "Has ingresado correctamente al sistema!")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Algo salió mal, intente nuevamente...")
            return redirect('login')
    return render(request, 'mod_login/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout exitoso!')
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario fue creado exitosamente!')
            return redirect('home')
    else:
        form = UserCreationForm()  # Initialize form if the request is not POST
    return render(request, 'mod_login/register_user.html', {'form': form})