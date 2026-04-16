from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm


def crear_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_eventos')
    return render(request, 'registrar_eventos/crear_evento.html', {'form': form ,'title': "Crear evento",})


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'registrar_eventos/listar_eventos.html', {'eventos': eventos, 'title': "Listar eventos",})
