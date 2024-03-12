from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Productos(models.Model):
    codigo_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.nombre_producto
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    descripcion_categoria = models.TextField(blank=True)
class clientes(models.Model):
    cedula = models.CharField(max_length=20,unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    gmail = models.EmailField()
class Empleados(models.Model):
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    gmail = models.EmailField()
class Ventas(models.Model):
    OPCIONES=[
        ('debito', 'debito'),
        ('efectivo', 'efectivo'),
        ('tarjeta de credito', 'tarjeta de credito'),
        ('psi', 'psi'),
        ('nequi', 'nequi'), 
    ]
    subtotal = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50,choices=OPCIONES)
    total = models.FloatField()
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
class Stock(models.Model):
    cantidad_stock = models.IntegerField()
    fecha_revision = models.CharField(max_length=100)
    fecha_reposicion = models.CharField(max_length=100)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
class Carrito(models.Model):
    nomproducto = models.IntegerField(max_length=100)
    precio = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    

