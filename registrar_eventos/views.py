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
            # (convertir errores a messages)
            for campo, errores in form.errors.items():
                for error in errores:
                    messages.error(request, f"Informacion de la actividad - {form.fields[campo].label}: {error}")
            
            for campo, errores in form_proyectado.errors.items():
                for error in errores:
                    messages.error(request, f"Presupuesto proyectado - {form_proyectado.fields[campo].label}: {error}")

            for campo, errores in form_ejecutado.errors.items():
                for error in errores:
                    messages.error(request, f"Presupuesto ejecutado - {form_ejecutado.fields[campo].label}: {error}")

    else:
        # Formularios vacíos para la carga inicial (GET)
        form = EventoForm()
        form_proyectado = PresupuestoForm(prefix='proyectado')
        form_ejecutado = PresupuestoForm(prefix='ejecutado')

    context = {
        'form': form,
        'form_proyectado': form_proyectado,
        'form_ejecutado': form_ejecutado,
        'evento': None , # Al ser None, el template dirá "Registrar"
        'title': "Crear evento"
    }
    return render(request, 'registrar_eventos/crear_evento.html', context)

#listar eventos
@login_required(login_url='login')
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'registrar_eventos/listar_eventos.html', {'eventos': eventos, 'title': "Listar eventos",})

# DETALLE EVENTO (CON TODO)
@login_required(login_url='login')
def detalle_evento(request, evento_id):
    # Obtener el evento o lanzar error 404
    evento = get_object_or_404(Evento, id=evento_id)

    # PRESUPUESTO proyectado: Traemos el presupuesto proyectado
    presu_proyectado = evento.presupuestos.filter(tipo='proyectado').first()
    
    # PRESUPUESTO ejecutado: Traemos el presupuesto ejecutado
    presu_ejecutado = evento.presupuestos.filter(tipo='ejecutado').first()

    # PREMIACIONES: Traemos todas las premiaciones del evento ordenadas
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

    # ENVIAR AL TEMPLATE
    
    return render(request, 'registrar_eventos/detalle_evento.html', {
        'evento': evento,
        'presu_p': presu_proyectado,
        'presu_e': presu_ejecutado,
        'categorias': categorias,
        'title': f"Detalle - {evento.nombre_actividad}"
    })

# EDITAR EVENTO ALL EN UNO
@login_required(login_url='login')
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    presu_proyectado = evento.presupuestos.filter(tipo='proyectado').first()
    presu_ejecutado = evento.presupuestos.filter(tipo='ejecutado').first()

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        form_proyectado = PresupuestoForm(request.POST, prefix='proyectado', instance=presu_proyectado)
        form_ejecutado = PresupuestoForm(request.POST, prefix='ejecutado', instance=presu_ejecutado)

        if form.is_valid() and form_proyectado.is_valid() and form_ejecutado.is_valid():
            form.save()

            presu_p = form_proyectado.save(commit=False)
            presu_p.evento = evento
            presu_p.tipo = 'proyectado'
            presu_p.save()

            presu_e = form_ejecutado.save(commit=False)
            presu_e.evento = evento
            presu_e.tipo = 'ejecutado'
            presu_e.save()

            messages.success(request, 'Evento actualizado correctamente')
            return redirect('detalle_evento', evento_id=evento.id)

    else:
        form = EventoForm(instance=evento)
        form_proyectado = PresupuestoForm(prefix='proyectado', instance=presu_proyectado)
        form_ejecutado = PresupuestoForm(prefix='ejecutado', instance=presu_ejecutado)

    return render(request, 'registrar_eventos/editar_evento.html', {
        'form': form,
        'form_proyectado': form_proyectado,
        'form_ejecutado': form_ejecutado,
        'evento': evento, # Al existir, el template dirá "Editar"
        'title': 'Editar evento'
    })

#crear participantes
@login_required(login_url='login')
def crear_participantes(request):
    form = ParticipanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Participante creado')
        return redirect('crear_participantes')
    return render(request, 'registrar_eventos/crear_participantes.html', {'form': form ,'title': "Crear participante",})

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
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })


# PREMIACIONES POR EVENTO
@login_required(login_url='login')
def gestionar_premiacion(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    form = PremiacionForm(request.POST or None)

    if request.method == 'POST':
        print("POST DATA:", request.POST)

    if form.is_valid():
        premiacion = form.save(commit=False)
        premiacion.evento = evento
        premiacion.save()
        
        messages.success(request, 'Premio agregado correctamente')
        return redirect('gestionar_premiacion', evento_id=evento.id)
   
    # Agrupar por categoría ( importante)
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

# EDITAR PREMIACIÓN CLÁSICO (PÁGINA SEPARADA) (EN DESUSO, SE DEJA SOLO COMO REFERENCIA DE CÓMO HACERLO SIN AJAX)
@login_required(login_url='login')
def editar_premiacion(request, premio_id):
    premio = get_object_or_404(Premiacion, id=premio_id)

    form = PremiacionForm(request.POST or None, instance=premio)

    if form.is_valid():
        form.save()
        messages.success(request, 'Premio actualizado')
        return redirect('detalle_evento', evento_id=premio.evento.id)

    return render(request, 'registrar_eventos/editar_premio.html', {
        'form': form,
        'premio': premio,
        'title': 'Editar premio'
    })

# EDITAR PREMIACIÓN AJAX (USADO EN EL MODAL, SE DEJA EL CLÁSICO SOLO COMO REFERENCIA DE CÓMO HACERLO SIN AJAX)
@login_required(login_url='login')
def editar_premio_ajax(request):
    try:
        premio = get_object_or_404(Premiacion, id=request.POST.get('id'))

        form = PremiacionForm(request.POST, instance=premio)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Premio actualizado correctamente'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': form.errors.as_json()
            })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

#eliminar premiacion modal
@login_required(login_url='login')
def delete_premio_ajax(request):
    try:
        premio_id = request.POST.get('id')

        if not premio_id:
            return JsonResponse({'status': 'error', 'message': 'No llegó el ID'})

        premio = Premiacion.objects.get(id=premio_id)
        premio.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Premio eliminado correctamente'
        })

    except Premiacion.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'El premio no existe'
        })

    except Exception as e:
        print("🔥 ERROR ELIMINAR:", e)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })