from django.shortcuts import render
from .modelmodels import *

# Create your views here.
def start(request):
    user_id= request.session.get('id_usuario')

    if user_id  is not None:

        usuario=Usuario.objects.get(id_usuario=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
            }
            return render(request, 'inicio/index.html', context)
       
    return render(request, 'index.html')

def reserva(request):
    user_id= request.session.get('id_usuario')

    if user_id  is not None:

        usuario = Usuario.objects.get(id_usuario=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
            }
            return render(request, 'reserva/index.html', context)
       
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro/index.html')