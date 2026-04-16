from django import forms
from .models import Evento, Participante, Premiacion, Presupuesto


# Definición de opciones para el campo de agencia
AGENCIA = [
    ('', 'Seleccionar'),
    ('MOCOA', 'Mocoa'),
    ('PUERTO ASIS', 'Puerto Asis'),
    ('DORADA', 'Dorada'),
    ('HORMIGA', 'Hormiga'),
    ('ORITO', 'Orito'),
    ('VILLA GARZON', 'Villa Garzon'),
    ('PUERTO LEGUIZAMO', 'Puerto Leguizamo'),
    ('SIBUNDOY', 'Sibundoy'),
]

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        # Solo incluimos los campos que REALMENTE existen en el modelo Evento
        fields = [
            'agencia', 'fecha_informe', 'tipo_actividad', 'nombre_actividad', 
            'fecha_actividad', 'lugar_actividad', 'cupo_participantes', 
            'asociados_participantes', 'acompanantes_participantes',
            'facilitador', 'entidad_aliada', 'programa_desarrollo', 'descripcion_ejecucion'
        ]
        
        labels = {
            'nombre_actividad': 'Nombre de la Actividad',
            'fecha_informe': 'Fecha del Informe',
            'cupo_participantes': 'Cupo Total',
        }

        widgets = {
            # Aplicamos clases de Bootstrap 'form-control' para que se vea bien
            'agencia': forms.Select(attrs={'class': 'form-control', 'id': 'agencia'}, choices=AGENCIA),
            'fecha_informe': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_actividad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Taller, Asamblea'}),
            'nombre_actividad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del evento'}),
            'fecha_actividad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lugar_actividad': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Campos numéricos
            'cupo_participantes': forms.NumberInput(attrs={'class': 'form-control'}),
            'asociados_participantes': forms.NumberInput(attrs={'class': 'form-control'}),
            'acompanantes_participantes': forms.NumberInput(attrs={'class': 'form-control'}),
            
            # Áreas de texto (ajustamos la altura con 'rows')
            'facilitador': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'entidad_aliada': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'programa_desarrollo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'descripcion_ejecucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

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