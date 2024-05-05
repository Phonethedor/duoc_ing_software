from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('reserva/', reserva, name='reserva'),
    path('reservar/', reservar, name='reservar'),
    path('reservas/', reservas, name='reservas'),
    path('registro/', registro, name='registro'),
    path('register/', register, name='register'),
    path('ingresar/', ingresar, name='ingresar'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cuenta/', cuenta, name='cuenta'),
    path('update_user/', update_user, name='update_user'),
    path('administrar/', administrar, name='administrar'),
    path('admin_crear_cuenta/', admin_crear_cuenta, name='admin_crear_cuenta'),
    path('admin_register/', admin_register, name='admin_register'),
]