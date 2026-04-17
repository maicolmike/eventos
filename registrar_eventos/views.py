from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm,ParticipanteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#crear evento
@login_required(login_url='login')
def crear_evento(request):
    form = EventoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Al llamar a save() directamente, Django guarda el Evento 
            # Y las relaciones ManyToMany (colaboradores/directivos) automáticamente.
            form.save() 
            messages.success(request, 'Evento creado')
            return redirect('listar_eventos')
    
    return render(request, 'registrar_eventos/crear_evento.html', {'form': form, 'title': "Crear evento"})

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

# detalle evento
@login_required(login_url='login')
def detalle_evento(request, evento_id):
    # Buscamos el evento o devolvemos un error 404 si no existe
    evento = get_object_or_404(Evento, id=evento_id)
    
    return render(request, 'registrar_eventos/detalle_evento.html', {
        'evento': evento,
        'title': f"Detalle - {evento.nombre_actividad}"
    })