from django.urls import path
from . import views

urlpatterns = [
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('listar_eventos/', views.listar_eventos, name='listar_eventos'),
    path('crear_participantes/', views.crear_participantes, name='crear_participantes'),
    path('listar_participantes/', views.listar_participantes, name='listar_participantes'),
    path('detalle/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('editar_participante/', views.editar_participante_ajax, name='editar_participante_ajax'),
    path('delete_participante/', views.delete_participante_ajax, name='delete_participante_ajax'),
]