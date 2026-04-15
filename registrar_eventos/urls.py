from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_evento, name='crear_evento'),
    path('listar/', views.listar_eventos, name='listar_eventos'),
]