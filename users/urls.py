from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('list_users/',views.list_users, name='list_users'),
    path('perfil/',views.perfil, name='perfil'),
    path('change_password/',views.change_password, name='change_password'),
    path('user_update_ajax/', views.user_update_ajax, name='user_update_ajax'),
    path('change_password_ajax/', views.change_password_ajax, name='change_password_ajax'),
]