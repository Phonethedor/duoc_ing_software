from django.contrib import admin
from .models import *

# Register your models here.
# super user: user= admin pass= admin

admin.site.register(Usuario)
admin.site.register(CategoriaHabitacion)
admin.site.register(Habitacion)
admin.site.register(MetodoPago)
admin.site.register(Reserva)