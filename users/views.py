from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginUser  # 👈 IMPORTANTE
from django.contrib.auth.decorators import login_required

#Inicio de sesion login
def login_view(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Bienvenido {}'.format(user.username))
                return redirect('index')  # Redirige al usuario a la página de inicio
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginUser()  # Crea un formulario vacío si la solicitud no es POST
    
    # Si el usuario ya está autenticado, redirige a la página de inicio
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'users/login.html', {
        'title': "Login eventos",
        'form': form
    })

#Cerrar de sesion login
def logout_view(request):
    logout(request)
    messages.error(request,'Sesion cerrada')
    return redirect('login')
