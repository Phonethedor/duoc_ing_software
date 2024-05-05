from django.urls import path
from .views import *

'''
    TODO:
    - agregar las urls restantes, luego de haber creado las vistas
'''

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
]