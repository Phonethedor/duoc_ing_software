from django.urls import path
from .views import *

urlpatterns = [
    path('', start, name='start'),
    path('reserva', reserva, name='reserva'),
]