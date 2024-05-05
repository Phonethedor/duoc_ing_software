from django.shortcuts import render, redirect
from .models import *

def start(request):
    user_id= request.session.get('id_usuario')

    if user_id  is not None:

        usuario = Usuario.objects.get(id_usuario=user_id) 
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
            return render(request, 'index.html', context)
    return render(request, 'reserva.html')

def registro(request):
    return render(request, 'registro.html')

'''
    prototipo de registro, sin testear
'''
def register(request):
    correo = request.POST['email']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    password = request.POST['password']

    Usuario.objects.create(email=correo, nombre=nombre, apellido=apellido,pass_usuario = password, tipo=2)
    return redirect('start')

def ingresar(request):
    return render(request, 'login.html')

'''
    prototipo de login, sin testear
'''
def  login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return redirect('ingresar')

    if user.password == password:
        request.session['id_usuario'] = user.id_usuario
        return redirect('start')
    else:
        return redirect('ingresar')
    
'''
    TODO:
    - testear login
    - testear registro
    - implementar logout
    - implementar registro de reservas (comun)
    - implementar registro de habitaciones (admin)
    - implementar modificacion de usuario (comun)
    - implementar modificacion de usuario (admin)
    - implementar modificacion de habitaciones (admin)
    - implementar vista de historial de reservas (admin)
'''