from django import forms
from .models import Evento, Participante, Premiacion, Presupuesto


# Definición de opciones para el campo de agencia
AGENCIA = [
    ('', ''),
    ('MOCOA', 'Mocoa'),
    ('PUERTO ASIS', 'Puerto Asis'),
    ('DORADA', 'Dorada'),
    ('HORMIGA', 'Hormiga'),
    ('ORITO', 'Orito'),
    ('VILLA GARZON', 'Villa Garzon'),
    ('PUERTO LEGUIZAMO', 'Puerto Leguizamo'),
    ('SIBUNDOY', 'Sibundoy'),
]

# Definición de opciones para el campo de agencia
TIPO_ACTIVIDAD = [
    ('', ''),
    ('BINGO FAMILIAR', 'Bingo familiar'),
    ('BINGO NINOS', 'Bingo niños'),
    ('CAPACITACION', 'Capacitación personal / directivos'),
    ('CBES', 'CBES'),
    ('COMETAS', 'Cometas'),
    ('CURSO CBES', 'Curso CBES'),
    ('CURSO COMPLEMENTARIO', 'Curso complementario'),
    ('ENCUENTRO', 'Encuentro'),
    ('MANUALIDADES', 'Manualidades'),
    ('PIN_ICFES', 'Pin icfes'),
    ('PROGRAMA RADIO', 'Programa radio'),
    ('OTROS', 'Otros'),
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
            'nombre_actividad': 'Nombre de la actividad',
            'fecha_informe': 'Fecha del informe',
            'cupo_participantes': 'Cupo total',
            'asociados_participantes': 'Número de asociados Participantes',
            'acompanantes_participantes': 'Número de acompañantes participantes',
        }

        widgets = {
            # Aplicamos clases de Bootstrap 'form-control' para que se vea bien
            'agencia': forms.Select(attrs={'class': 'form-control', 'id': 'agencia'}, choices=AGENCIA),
            'fecha_informe': forms.DateInput(attrs={'class': 'form-control', 'id': 'fecha_informe', 'type': 'date'}),
            'tipo_actividad': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_actividad'}, choices=TIPO_ACTIVIDAD),
            'nombre_actividad': forms.TextInput(attrs={'class': 'form-control',}),
            'fecha_actividad': forms.DateInput(attrs={'class': 'form-control', 'id': 'fecha_actividad', 'type': 'date'}),
            'lugar_actividad': forms.TextInput(attrs={'class': 'form-control',}),
            
            # Campos numéricos
            'cupo_participantes': forms.NumberInput(attrs={'class': 'form-control',}),
            'asociados_participantes': forms.NumberInput(attrs={'class': 'form-control',}),
            'acompanantes_participantes': forms.NumberInput(attrs={'class': 'form-control',}),
            
            # Áreas de texto (ajustamos la altura con 'rows')
            'facilitador': forms.TextInput(attrs={'class': 'form-control',}),
            'entidad_aliada': forms.TextInput(attrs={'class': 'form-control',}),
            'programa_desarrollo': forms.TextInput(attrs={'class': 'form-control',}),
            'descripcion_ejecucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,}),
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