from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginUser, RegistroUsuarioForm,EditarPerfilForm,CambiarClaveForm
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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
@login_required(login_url='login') 
def logout_view(request):
    logout(request)
    messages.error(request,'Sesion cerrada')
    return redirect('login')

#Registrar usuario
@login_required(login_url='login')    
def register(request):
    form = RegistroUsuarioForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save() #save () se encuentra en el archivo forms.py
        if user:
            if form.cleaned_data['is_superuser'] == '1': #El campo en el formulario html es 1
                #otorgar permisos de administrador
                user.is_staff = True
                user.is_superuser = True
            user.save()
            messages.success(request, 'usuario creado')
            return redirect('register')
    
    return render(request, 'users/register.html', {
        'form': form,
        'title': "Registro",
        })

#Listar usuarios
@login_required(login_url='login')
def list_users(request):
    lista_usuarios = User.objects.all()
    return render(request, 'users/list_users.html',{ 
        'title': "Listado Usuarios",
        'lista_usuarios': lista_usuarios,
    })
#Editar perfil
@login_required(login_url='login')    
def perfil(request):
    user = request.user

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save(commit=False)

            # 🔒 BLOQUEO TOTAL (aunque manipulen el HTML)
            user.username = request.user.username
            user.is_superuser = request.user.is_superuser

            user.save()

            messages.success(request, 'Perfil actualizado exitosamente.')

    else:
        form = EditarPerfilForm(instance=user)

    return render(request, 'users/perfil.html', {
        'form': form,
        'title': 'Editar perfil'
    })

#cambiar clave
@login_required(login_url='login')    
def change_password(request):
    
    form = CambiarClaveForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        password_actual = form.cleaned_data['passwordActual']
        password_nueva = form.cleaned_data['passwordNew']
        confirmar_password = form.cleaned_data['passwordNewConfirm']

        # Validar que la contraseña actual sea correcta
        if not request.user.check_password(password_actual):
            messages.error(request, 'La contraseña actual es incorrecta.')
            return render(request, 'users/change_password.html', {'form': form, 'title': 'Cambiar clave'})
        
        # Validar que la contraseña actual sea diferente de la nueva
        if password_actual == password_nueva:
            messages.error(request, 'La nueva contraseña debe ser diferente de la contraseña actual.')
            return render(request, 'users/change_password.html', {'form': form, 'title': 'Cambiar clave'})
        
        # Validar que la nueva contraseña y la confirmación coincidan
        if password_nueva != confirmar_password:
            messages.error(request, 'La nueva contraseña y confirmacion de contraseña no coinciden.')
            return render(request, 'users/change_password.html', {'form': form, 'title': 'Cambiar clave'})

        # Cambiar la contraseña del usuario
        request.user.set_password(password_nueva)   #request.user es específico para interactuar con el usuario que ha iniciado sesión en ese momento, 
        request.user.save()

        # Actualizar la sesión del usuario para evitar cerrar sesión después de cambiar la contraseña
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Contraseña cambiada exitosamente.')

    return render(request, 'users/change_password.html', {'form': form, 'title': 'Cambiar clave'})

#Actualizar usuario con ajax
@login_required(login_url='login')
def user_update_ajax(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')

        user = get_object_or_404(User, id=user_id)

        username = request.POST.get('username')
        identificacion = request.POST.get('identificacion')

        # Validaciones
        if User.objects.filter(username=username).exclude(id=user_id).exists():
            return JsonResponse({'status': 'error', 'message': 'El usuario ya existe'})

        if User.objects.filter(identificacion=identificacion).exclude(id=user_id).exists():
            return JsonResponse({'status': 'error', 'message': 'La identificación ya existe'})

        # Actualizar
        user.identificacion = identificacion
        user.nombres = request.POST.get('nombres')
        user.username = username
        user.email = request.POST.get('userEmail')
        user.agencia = request.POST.get('agencia')
        user.is_superuser = bool(int(request.POST.get('tipousuario')))
        user.is_active = bool(int(request.POST.get('estado')))
        user.save()

        return JsonResponse({'status': 'success', 'message': 'Usuario actualizado correctamente'})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})