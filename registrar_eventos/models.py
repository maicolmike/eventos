from django.db import models

# Create your models here.


# 1. Define la lista AQUÍ afuera para que todos los modelos la vean
AGENCIAS = [
    ('mocoa', 'Mocoa'),
    ('sibundoy', 'Sibundoy'),
    ('puerto_asis', 'Puerto Asis'),
    ('hormiga', 'Hormiga'),
    ('orito', 'Orito'),
    ('leguizamo', 'Leguizamo'),
    ('dorada', 'Dorada'),
    ('villagarzon', 'Villagarzon'),
]

class Evento(models.Model):
    agencia = models.CharField(max_length=50, choices=AGENCIAS)
    fecha_informe = models.DateTimeField()
    tipo_actividad = models.CharField(max_length=100)
    nombre_actividad = models.TextField()
    fecha_actividad = models.DateTimeField()
    lugar_actividad = models.CharField(max_length=255)

    cupo_participantes = models.IntegerField()
    asociados_participantes = models.IntegerField()
    acompanantes_participantes = models.IntegerField()

    facilitador = models.TextField(blank=True)
    entidad_aliada = models.TextField(blank=True)
    programa_desarrollo = models.TextField(blank=True)
    descripcion_ejecucion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_actividad

class Participante(models.Model):
    TIPO_PARTICIPANTE = [
        ('colaborador', 'Colaborador'),
        ('directivo', 'Directivo'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')
    tipo_participante = models.CharField(max_length=20, choices=TIPO_PARTICIPANTE)

    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50, choices=AGENCIAS)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Presupuesto(models.Model):
    TIPOS = [
        ('proyectado', 'Proyectado'),
        ('ejecutado', 'Ejecutado'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='presupuestos')
    tipo = models.CharField(max_length=20, choices=TIPOS)

    refrigerio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    almuerzo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    publicidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sonido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    video = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    premiacion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imprevistos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    otros = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_proyecto = models.DecimalField(max_digits=12, decimal_places=2)
    total_presupuesto = models.DecimalField(max_digits=12, decimal_places=2)

class Premiacion(models.Model):
    CATEGORIAS = [
        ('infantil', 'Infantil'),
        ('juvenil', 'Juvenil'),
        ('libre', 'Libre'),
    ]
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='premiaciones')
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50, choices=AGENCIAS)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    puesto_numero = models.IntegerField()
    valor_premio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"