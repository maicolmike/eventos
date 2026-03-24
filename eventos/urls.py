from django.contrib import admin
from django.urls import path, include
from . import views # se importa la vista creada en views.py para que pueda ser utilizada en urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    #agregadas por el usuario
    path('', views.index, name='index'),
    path('users/', include('users.urls')), # se agrega esta linea para que reconozca las urls de la app users
]
