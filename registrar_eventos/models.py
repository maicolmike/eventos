from django.db import models

# Create your models here.
class Evento(models.Model):
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

    agencia = models.CharField(max_length=50, choices=AGENCIAS)
    fecha_informe = models.DateTimeField()
    tipo_actividad = models.CharField(max_length=100)
    nombre = models.TextField()
    fecha_actividad = models.DateTimeField()
    lugar = models.CharField(max_length=255)

    cupo = models.IntegerField()
    asociados = models.IntegerField()
    acompanantes = models.IntegerField()

    facilitador = models.TextField(blank=True)
    entidad = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


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

    valor_total = models.DecimalField(max_digits=12, decimal_places=2)


class Participante(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50)

    es_colaborador = models.BooleanField(default=False)
    es_directivo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Ganador(models.Model):
    CATEGORIAS = [
        ('infantil', 'Infantil'),
        ('juvenil', 'Juvenil'),
        ('libre', 'Libre'),
    ]
    valor_premio = models.DecimalField(max_digits=10, decimal_places=2)