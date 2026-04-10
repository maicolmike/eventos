from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginUser, RegistroUsuarioForm,EditarPerfilForm,CambiarClaveForm, LoginUserRecuperarClave
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# importaciones para envio de correo
import random
import string
from threading import Thread
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

            # BLOQUEO TOTAL (aunque manipulen el HTML)
            user.username = request.user.username
            user.is_superuser = request.user.is_superuser

            user.save()

            messages.success(request, 'Perfil actualizado exitosamente.')

    else:
        form = EditarPerfilForm(instance=user)

    return render(request, 'users/perfil.html', {
        'form': form,
        'title': 'Mi perfil'
    })

#cambiar contraseña
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

# CAMBIAR CLAVE DESDE LISTADO (AJAX)
@login_required(login_url='login')
def change_password_ajax(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        # Validación básica para asegurarnos de que se recibió el ID del usuario
        if not user_id:
            return JsonResponse({
                'status': 'error',
                'message': 'ID de usuario no recibido'
                })
        nueva_password = request.POST.get('password')

        user = get_object_or_404(User, id=user_id)

        # VALIDACIÓN BÁSICA
        if not nueva_password or len(nueva_password) < 4:
            return JsonResponse({
                'status': 'error',
                'message': 'La contraseña debe tener al menos 4 caracteres'
            })

        # CAMBIAR CLAVE
        user.set_password(nueva_password)
        user.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Contraseña actualizada correctamente'
        })

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

# ELIMINAR USUARIO (AJAX)
@login_required(login_url='login')
def delete_user_ajax(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')

        if not user_id:
            return JsonResponse({
                'status': 'error',
                'message': 'ID no recibido'
            })

        user = get_object_or_404(User, id=user_id)

        # 🔒 OPCIONAL: evitar que se elimine a sí mismo
        if user == request.user:
            return JsonResponse({
                'status': 'error',
                'message': 'No puedes eliminar tu propio usuario'
            })

        user.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Usuario eliminado correctamente'
        })

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

# generar clave automatica   
def generate_random_password(length=8):
    # Define un conjunto de caracteres que incluye letras (mayúsculas y minúsculas), dígitos y algunos caracteres especiales.
    characters = string.ascii_letters + string.digits + "*#$&!?"
    
    # Genera una contraseña aleatoria de 6 caracteres eligiendo aleatoriamente de los caracteres definidos.
    return ''.join(random.SystemRandom().choice(characters) for _ in range(length))

# Función para enviar el correo electrónico con la nueva contraseña al usuario.
def send_password_email(user, new_password):
    # Asunto del correo electrónico.
    subject = 'Recuperación de Contraseña'
    
    # Renderiza la plantilla HTML con los datos necesarios.
    html_message = render_to_string('emails/restablecerclave.html', {'username': user.username, 'nombres': user.nombres,'new_password': new_password})
    
    # Convierte el mensaje HTML a texto plano.
    plain_message = strip_tags(html_message)
    
    # Dirección de correo electrónico del remitente personalizada.
    from_email = "servicio de notificación <{}>".format(settings.DEFAULT_FROM_EMAIL)
    
    # Lista de destinatarios.
    recipient_list = [user.email]
    
    # Envía el correo electrónico con el asunto, mensaje en texto plano, mensaje HTML, remitente y lista de destinatarios.
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

# recuperar clave  
def recuperar_clave(request):
    # Verifica si la solicitud es de tipo POST (es decir, si se ha enviado el formulario).
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados.
        form = LoginUserRecuperarClave(request.POST)
        
        # Verifica si el formulario es válido.
        if form.is_valid():
            # Obtiene el nombre de usuario ingresado en el formulario.
            username = form.cleaned_data['username']
            try:
                # Intenta obtener al usuario de la base de datos por su nombre de usuario.
                user = User.objects.get(username=username)

                # VALIDAR EMAIL
                if not user.email:
                    messages.error(request, 'El usuario no tiene correo registrado.')
                    return redirect('login')

                # Genera una nueva contraseña aleatoria.
                new_password = generate_random_password()
                
                # Establece la nueva contraseña para el usuario.
                user.set_password(new_password)
                
                # Guarda los cambios en la base de datos.
                user.save()

                # Envía la nueva contraseña al correo electrónico del usuario en segundo plano
                Thread(target=send_password_email, args=(user, new_password)).start()

                # Muestra un mensaje de éxito al usuario.
                #messages.success(request, f'Se ha enviado un correo para recuperar su clave.')
                
                # Redirige al usuario a la página de inicio de sesión.
                #return redirect('login')
            except User.DoesNotExist:
                # SEGURIDAD: NO revelar si existe o no
                pass
                #messages.success(request, f'Se ha enviado un correo para recuperar su clave.')
                # Redirige al usuario a la página de inicio de sesión.
                #return redirect('login')

            # ✅ MENSAJE ÚNICO (BUENA PRÁCTICA)
            messages.success(request, 'Si el usuario existe, se ha enviado un correo para recuperar la clave.')
            return redirect('login')
        else:
            # Si el formulario no es válido, muestra un mensaje de error.
            messages.error(request, 'Formulario inválido.')
    else:
        # Si la solicitud no es de tipo POST, simplemente crea un formulario vacío.
        form = LoginUserRecuperarClave()

    # Renderiza la plantilla recuperarClave.html con el formulario.
    return render(request, 'users/recuperarClave.html', {
        'title': "Recuperar clave",
        'form': form,
    })

