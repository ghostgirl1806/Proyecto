from django.forms import ModelForm
from django import forms
from .models import Productos, clientes, Carrito

class producform(ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo_producto', 'nombre_producto', 'categoria', 'descripcion','precio', 'cantidad']
class clientform(ModelForm):
    class Meta:
        model = clientes
        fields = ['cedula', 'nombres', 'apellidos', 'direccion','telefono', 'gmail']
class carritoform(ModelForm):
    class Meta:
        model = Carrito
        fields = ['nomproducto', 'precio', 'cantidad']
class AgregarAlCarritoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, initial=1)