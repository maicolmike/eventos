from django import forms
from .models import Evento, Participante, Ganador, Presupuesto

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

class GanadorForm(forms.ModelForm):
    class Meta:
        model = Ganador
        fields = '__all__'

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'