from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    tipo = models.IntegerField(default=2)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class CategoriaHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    disponible = models.BooleanField()
    categoria = models.ForeignKey(CategoriaHabitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):  
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.nombre + ' ' + self.usuario.apellido + ' ' + self.habitacion.nombre
    