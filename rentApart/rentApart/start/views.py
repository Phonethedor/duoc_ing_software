from django.shortcuts import render, redirect
from .models import *

'''
    TODO:
    - implementar registro de reservas (comun)
    - implementar registro de habitaciones (admin)
    - implementar modificacion de usuario (comun)
    - implementar modificacion de usuario (admin)
    - implementar modificacion de habitaciones (admin)
    - implementar vista de historial de reservas (admin)
'''

def index(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
            }
            return render(request, 'index.html', context)
    return render(request, 'index.html')

def reserva(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        habitaciones = Habitacion.objects.all()
        metodos_pago = MetodoPago.objects.all()
        if usuario:
            context = {
                "usuario": usuario,
                "habitaciones": habitaciones,
                "metodos_pago": metodos_pago,
            }
            return render(request, 'reserva.html', context)
    return redirect(request, 'index')

# Metodo de reserva, cambia estado de habitacion y redirecciona a index
def reservar(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        habitacion_id = request.POST.get('habitacion')
        metodo_pago_id = request.POST.get('metodo_pago')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        habitacion = Habitacion.objects.get(id=habitacion_id)
        metodo_pago = MetodoPago.objects.get(id=metodo_pago_id)

        Reserva.objects.create(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, habitacion=habitacion, usuario=usuario, metodo_pago=metodo_pago)
        habitacion.disponible = False
        habitacion.save()
        return redirect('index')
    return redirect('index')

def registro(request):
    return render(request, 'registro.html')

# Metodo de registro, redirecciona a index
def register(request):
    correo = request.POST['email']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    password = request.POST['password']

    Usuario.objects.create(email=correo, nombre=nombre, apellido=apellido, password = password, tipo=2)
    return redirect('index')

def ingresar(request):
    return render(request, 'login.html')

# Metodo de login, redirecciona a index si se logra, sino a ingresar
def  login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return redirect('ingresar')

    if user.password == password:
        request.session['id'] = user.id
        return redirect('index')
    else:
        return redirect('ingresar')
    

# Metodo de logout, redirecciona a index
def logout(request):
    request.session.flush()
    return redirect('index')
