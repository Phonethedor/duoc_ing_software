from django.urls import path
from .views import *

'''
    TODO:
    - agregar las urls restantes, luego de haber creado las vistas
'''

urlpatterns = [
    path('', start, name='index'),
    path('reserva/', reserva, name='reserva'),
    path('registro/', registro, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
]