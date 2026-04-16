from django import forms
from .models import Evento, Participante, Premiacion, Presupuesto

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

class PremiacionForm(forms.ModelForm):
    class Meta:
        model = Premiacion
        fields = '__all__'

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'