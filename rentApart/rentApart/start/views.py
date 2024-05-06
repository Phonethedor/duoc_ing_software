from django.shortcuts import render, redirect
from .models import *

'''
    TODO:
    - implementar modificacion de habitaciones (admin)
    - implementar vista de historial de reservas por habitacion (admin)
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

# Metodo para eliminar usuario a travez de su id (admin)
def admin_eliminar_usuario(request):
    user_id= request.POST['id']

    if user_id  is not None:
            
            usuario = Usuario.objects.get(id=user_id)             
            usuario.delete()

            return redirect('administrar')
    return redirect('index')

# metodo para mostrar formulario de registro de habitacion (admin)
def admin_crear_habitacion(request):
    user_id= request.session.get('id')
    Categorias = CategoriaHabitacion.objects.all()
    if user_id  is not None:
            
            usuario = Usuario.objects.get(id=user_id) 
            if usuario:
                context = {
                    "usuario": usuario,
                    "categorias": Categorias,
                }
                return render(request, 'admin_crear_habitacion.html', context)
    return redirect('index')

# Metodo de registro de habitacion (admin), redirecciona a administrar
def admin_register_habitacion(request):
    user_id= request.session.get('id')

    if user_id  is not None:
            
            usuario = Usuario.objects.get(id=user_id) 
            if usuario:
                nombre = request.POST['nombre']
                precio = request.POST['precio']
                disponible = True
                categoria_habitacion = request.POST['categoria']
                categoria = CategoriaHabitacion.objects.get(id=categoria_habitacion)

                Habitacion.objects.create(nombre=nombre, precio=precio, disponible=disponible, categoria=categoria)
                return redirect('administrar')
    return redirect('index')

# Metodo para eliminar habitacion a travez de su id (admin)
def admin_eliminar_habitacion(request):
    habitacion_id= request.POST['id']

    if habitacion_id  is not None:
            
            habitacion = Habitacion.objects.get(id=habitacion_id)             
            habitacion.delete()

            return redirect('administrar')
    return redirect('index')

# Metodo para mostrar formulario para modificar usuario a travez de su id (admin)
def admin_editar_usuario(request):
    user_id = request.session.get('id')
    user_mod_id= request.POST['id']

    usuario= Usuario.objects.get(id=user_id)
    usuario_modificar = Usuario.objects.get(id=user_mod_id) 
    if usuario:
        context = {
            "usuario": usuario,
            "usuario_modificar": usuario_modificar,
        }
        return render(request, 'admin_cuenta.html', context)
    return redirect('index')

def admin_cuenta_update(request):
    user_id= request.session.get('id')

    if user_id  is not None:

        id = request.POST['id']
        usuario = Usuario.objects.get(id=id) 
        if usuario:
            correo = request.POST['email']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            password = request.POST['password']
            tipo = request.POST['tipo']

            usuario.email = correo
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.password = password
            usuario.tipo = tipo
            usuario.save()
            return redirect('administrar')
    return redirect('index')