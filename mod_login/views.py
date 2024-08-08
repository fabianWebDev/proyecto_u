from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('lista_ordenes')  # or another page suitable for logged-in users

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Has ingresado exitosamente al sistema!")
            return redirect('lista_ordenes')
        else:
            messages.error(request, "Algo salió mal, intente nuevamente...")
            return redirect('login')
    return render(request, 'mod_login/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, '¡Logout exitoso!')
    return redirect('lista_ordenes')

@login_required
def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El usuario fue creado exitosamente!')
            return redirect('register')
    else:
        form = CustomUserCreationForm()  # Initialize the form if the request is not POST
    return render(request, 'mod_login/register_user.html', {'form': form})
