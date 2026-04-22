from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import Evento, Participante, Presupuesto, Premiacion
from .forms import EventoForm,ParticipanteForm,PresupuestoForm,PremiacionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

#crear evento
@login_required(login_url='login')
def crear_evento(request):
    if request.method == 'POST':
        # Instanciamos los 3 formularios con los datos del POST
        form = EventoForm(request.POST)
        # El prefix es fundamental para separar los datos en el request.POST
        form_proyectado = PresupuestoForm(request.POST, prefix='proyectado')
        form_ejecutado = PresupuestoForm(request.POST, prefix='ejecutado')

        if form.is_valid() and form_proyectado.is_valid() and form_ejecutado.is_valid():
            # 1. Guardamos el evento (esto incluye los ManyToMany de participantes)
            evento = form.save()

            # 2. Guardamos presupuesto Proyectado
            presu_p = form_proyectado.save(commit=False)
            presu_p.evento = evento
            presu_p.tipo = 'proyectado'
            presu_p.save()

            # 3. Guardamos presupuesto Ejecutado
            presu_e = form_ejecutado.save(commit=False)
            presu_e.evento = evento
            presu_e.tipo = 'ejecutado'
            presu_e.save()

            messages.success(request, 'Evento y presupuestos registrados correctamente')
            return redirect('listar_eventos')

        else:
            # 🔥 AQUÍ ESTÁ LA MAGIA (convertir errores a messages)
            
            for campo, errores in form_proyectado.errors.items():
                for error in errores:
                    messages.error(request, f"Proyectado - {form_proyectado.fields[campo].label}: {error}")

            for campo, errores in form_ejecutado.errors.items():
                for error in errores:
                    messages.error(request, f"Ejecutado - {campo}: {error}")

            for campo, errores in form.errors.items():
                for error in errores:
                    messages.error(request, f"Evento - {campo}: {error}")

    else:
        # Formularios vacíos para la carga inicial (GET)
        form = EventoForm()
        form_proyectado = PresupuestoForm(prefix='proyectado')
        form_ejecutado = PresupuestoForm(prefix='ejecutado')

    context = {
        'form': form,
        'form_proyectado': form_proyectado,
        'form_ejecutado': form_ejecutado,
        'title': "Crear evento integral"
    }
    return render(request, 'registrar_eventos/crear_evento.html', context)

#listar eventos
@login_required(login_url='login')
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'registrar_eventos/listar_eventos.html', {'eventos': eventos, 'title': "Listar eventos",})

#crear evento
@login_required(login_url='login')
def crear_participantes(request):
    form = ParticipanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Participante creado')
        return redirect('crear_participantes')
    return render(request, 'registrar_eventos/crear_participantes.html', {'form': form ,'title': "Crear participante",})

# ================================
# DETALLE EVENTO (CON TODO)
# ================================
@login_required(login_url='login')
def detalle_evento(request, evento_id):
    # 🔹 Obtener el evento o lanzar error 404
    evento = get_object_or_404(Evento, id=evento_id)

    # ================================
    # 🔹 PRESUPUESTOS
    # ================================
    # Traemos el presupuesto proyectado
    presu_proyectado = evento.presupuestos.filter(tipo='proyectado').first()
    
    # Traemos el presupuesto ejecutado
    presu_ejecutado = evento.presupuestos.filter(tipo='ejecutado').first()

    # ================================
    # 🔹 PREMIACIONES
    # ================================
    # Traemos todas las premiaciones del evento ordenadas
    premiaciones = evento.premiaciones.all().order_by('categoria', 'puesto_numero')

    # Creamos estructura por categorías
    categorias = {
        'infantil': [],
        'juvenil': [],
        'libre': []
    }

    # Agrupamos manualmente
    for p in premiaciones:
        categorias[p.categoria].append(p)

    # ================================
    # 🔹 ENVIAR AL TEMPLATE
    # ================================
    return render(request, 'registrar_eventos/detalle_evento.html', {
        'evento': evento,
        'presu_p': presu_proyectado,
        'presu_e': presu_ejecutado,
        'categorias': categorias,
        'title': f"Detalle - {evento.nombre_actividad}"
    })

#listar participantes
@login_required(login_url='login')
def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'registrar_eventos/listar_participantes.html', {'lista_participantes': participantes, 'title': "Listar participantes",})

#editar participantes modal
@login_required(login_url='login')
def editar_participante_ajax(request):
    try:
        participante_id = request.POST.get('id')

        if not participante_id:
            return JsonResponse({'status': 'error', 'message': 'No llegó el ID'})

        participante = Participante.objects.get(id=participante_id)

        participante.tipo_participante = request.POST.get('tipo_participante')
        participante.identificacion = request.POST.get('identificacion')
        participante.nombres = request.POST.get('nombres')
        participante.apellidos = request.POST.get('apellidos')
        participante.agencia = request.POST.get('agencia')

        participante.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Participante actualizado correctamente'
        })

    except Exception as e:
        print("🔥 ERROR REAL:", e)  # 👈 IMPORTANTE
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

#eliminar participantes modal
@login_required(login_url='login')
def delete_participante_ajax(request):
    try:
        participante_id = request.POST.get('id')

        if not participante_id:
            return JsonResponse({'status': 'error', 'message': 'No llegó el ID'})

        participante = Participante.objects.get(id=participante_id)
        participante.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Participante eliminado correctamente'
        })

    except Participante.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'El participante no existe'
        })

    except Exception as e:
        print("🔥 ERROR ELIMINAR:", e)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

# ================================
# PREMIACIONES POR EVENTO
# ================================
@login_required(login_url='login')
def gestionar_premiacion(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    form = PremiacionForm(request.POST or None)

    if request.method == 'POST':
        print("POST DATA:", request.POST)  # 👈 DEBUG

    if form.is_valid():
        premiacion = form.save(commit=False)
        premiacion.evento = evento
        premiacion.save()
        print("✅ GUARDÓ")
        
        messages.success(request, 'Premio agregado correctamente')
        return redirect('gestionar_premiacion', evento_id=evento.id)
    else:
        print("❌ ERRORES:", form.errors)  # 👈 CLAVE

    # Agrupar por categoría (🔥 importante)
    premiaciones = evento.premiaciones.all().order_by('categoria', 'puesto_numero')

    categorias = {
        'infantil': [],
        'juvenil': [],
        'libre': []
    }

    for p in premiaciones:
        categorias[p.categoria].append(p)

    return render(request, 'registrar_eventos/premiacion.html', {
        'evento': evento,
        'form': form,
        'categorias': categorias,
        'title': f"Premiación - {evento.nombre_actividad}"
    })