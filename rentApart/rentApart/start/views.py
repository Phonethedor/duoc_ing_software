from django.shortcuts import render, redirect
from .models import *

'''
    TODO:
    - implementar registro de habitaciones (admin)
    - implementar registro  de usuarios (admin)
    - implementar modificacion de usuario (admin)
    - implementar modificacion de habitaciones (admin)
    - implementar vista de historial de reservas (admin)
'''

# Metodo para mostrar index
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

# metodo para mostrar formulario de reserva
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

# Metodo para mostrar reservas de usuario
def reservas(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        reservas = Reserva.objects.filter(usuario=usuario)
        if usuario:
            context = {
                "usuario": usuario,
                "reservas": reservas,
            }
            return render(request, 'reservas.html', context)
    return redirect('index')

# Metodo para mostrar formulario de registro
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

# Metodo para mostrar formulario de login
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

# Metodo para mostrar cuenta de usuario
def cuenta(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
            }
            return render(request, 'cuenta.html', context)
    return redirect('index')

# Metodo para actualizar usuario
def update_user(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        if usuario:
            correo = request.POST['email']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            password = request.POST['password']

            usuario.email = correo
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.password = password
            usuario.save()
            return redirect('cuenta')
    return redirect('index')

# Metodo para mostrar menu de administracion
def administrar(request):
    user_id= request.session.get('id')
    usuarios = Usuario.objects.all()
    habitaciones = Habitacion.objects.all()

    if user_id  is not None:

        usuario = Usuario.objects.get(id=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
                "usuarios": usuarios,
                "habitaciones": habitaciones,
            }
            return render(request, 'admin.html', context)
    return redirect('index')

# Metodo para mostrar formulario de registro de usuario (admin)
def admin_crear_cuenta(request):
    user_id= request.session.get('id')

    if user_id  is not None:
            
            usuario = Usuario.objects.get(id=user_id) 
            if usuario:
                context = {
                    "usuario": usuario,
                }
                return render(request, 'admin_crear_cuenta.html', context)
    return redirect('index')

# Metodo de registro de usuario (admin), redirecciona a administrar
def admin_register(request):
    correo = request.POST['email']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    password = request.POST['password']
    tipo = request.POST['tipo']

    Usuario.objects.create(email=correo, nombre=nombre, apellido=apellido, password = password, tipo=tipo)
    return redirect('administrar')