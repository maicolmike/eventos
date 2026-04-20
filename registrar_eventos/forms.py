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

# Definición de opciones para el campo de categoría en premiación
CATEGORIAS = [
        ('', ''),
        ('infantil', 'Infantil'),
        ('juvenil', 'Juvenil'),
        ('libre', 'Libre'),
    ]

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        # Solo incluimos los campos que REALMENTE existen en el modelo Evento
        fields = [
            'agencia', 'fecha_informe', 'tipo_actividad', 'nombre_actividad', 
            'fecha_actividad', 'lugar_actividad', 'cupo_participantes', 
            'asociados_participantes', 'acompanantes_participantes',
            'facilitador', 'entidad_aliada', 'programa_desarrollo', 'descripcion_ejecucion','colaboradores', 'directivos'
        ]
        
        labels = {
            'nombre_actividad': 'Nombre de la actividad',
            'fecha_informe': 'Fecha del informe',
            'cupo_participantes': 'Cupo total',
            'asociados_participantes': '#asociados participantes',
            'acompanantes_participantes': '#acompañantes participantes',
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
            
            # 2. Definimos los SelectMultiple para Select2
            'colaboradores': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'directivos': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }
    # Excluimos los campos de relaciones ManyToMany para manejarlos manualmente en la vista
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        # Filtramos para que en cada cuadro solo salgan los que corresponden
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
        
    # Método para validar un campo específico
    def clean_identificacion(self):
        # Obtenemos el dato que el usuario escribió
        identificacion = self.cleaned_data.get('identificacion')
        
        # Verificamos si ya existe en la base de datos
        # self.instance.pk nos permite excluir al propio registro si estamos editando
        if Participante.objects.filter(identificacion=identificacion).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un participante registrado con esta identificación.")
        
        # Siempre debes retornar el valor limpio
        return identificacion

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        exclude = ['evento', 'tipo'] # Excluimos evento y tipo porque se llenan automáticamente en la vista
        labels = {
            'refrigerio': 'Valor refrigerio',
            'almuerzo': 'Valor almuerzo',
            'publicidad': 'Valor publicidad',
            'sonido': 'Valor sonido',
            'video': 'Valor video',
            'premiacion': 'Valor premiación',
            'imprevistos': 'Valor imprevistos',
            'otros': 'Valor otros',
            'valor_proyecto': 'Valor total del proyecto',
            'total_presupuesto': 'Total del presupuesto',
        }
        widgets = {
            'refrigerio': forms.NumberInput(attrs={'class': 'form-control'}),
            'almuerzo': forms.NumberInput(attrs={'class': 'form-control'}),
            'publicidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'sonido': forms.NumberInput(attrs={'class': 'form-control'}),
            'video': forms.NumberInput(attrs={'class': 'form-control'}),
            'premiacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'imprevistos': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_proyecto': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_presupuesto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PremiacionForm(forms.ModelForm):
    class Meta:
        model = Premiacion
        exclude = ['evento']  # 👈 🔥 SOLUCIÓN CLAVE
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'agencia': forms.Select(attrs={'class': 'form-control'}, choices=AGENCIA),
            'categoria': forms.Select(attrs={'class': 'form-control'}, choices=CATEGORIAS),
            'puesto_numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_premio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

