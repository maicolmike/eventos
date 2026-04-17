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

# Definición de opciones para el campo de tipo de participante
TIPO_PARTICIPANTE = [
        ('', ''),
        ('colaborador', 'Colaborador'),
        ('directivo', 'Directivo'),
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
            
            # Para los campos de relaciones ManyToMany, usaremos SelectMultiple
            'colaboradores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'directivos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        # Excluimos los campos de relaciones ManyToMany para manejarlos manualmente en la vista
        def __init__(self, *args, **kwargs):
            super(EventoForm, self).__init__(*args, **kwargs)
            # Filtramos los participantes para que solo aparezcan según su tipo
            self.fields['colaboradores'].queryset = Participante.objects.filter(tipo_participante='colaborador')
            self.fields['directivos'].queryset = Participante.objects.filter(tipo_participante='directivo')

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'
        widgets = {
            'tipo_participante': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_participante'}, choices=TIPO_PARTICIPANTE),
            'nombres': forms.TextInput(attrs={'class': 'form-control',}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control',}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control',}),
            'agencia': forms.Select(attrs={'class': 'form-control', 'id': 'agencia'}, choices=AGENCIA),
        }

class PremiacionForm(forms.ModelForm):
    class Meta:
        model = Premiacion
        fields = '__all__'

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'