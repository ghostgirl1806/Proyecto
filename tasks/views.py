import re
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Productos, clientes,Carrito
from .forms import producform, clientform, AgregarAlCarritoForm
from django.utils import timezone
from dotenv import load_dotenv
from email.message import EmailMessage
import os
import smtplib
import ssl
# Create your views here.

@login_required
def home(request):
    
    Producto = Productos.objects.all()
    return render(request, 'home.html',{'productos':Producto})

def is_valid_password(password):
    # La contraseña debe tener al menos 8 caracteres
    # Debe contener al menos una letra mayúscula, una letra minúscula y un carácter especial
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(regex.match(password))

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2 and len(password1) >= 8 and is_valid_password(password1):
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=password1,email=email)
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'El usuario ya existe'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'La contraseña no cumple con los requisitos'})
    
def email(email):
    load_dotenv()
    email_sender = "martinezaleja180220@gmail.com"
    password =  os.getenv("PASSWORD")
    email_reciver = email
    subject = "NOTIFICACION INICIO DE SESION"
    body = f""" Un usuario esta ingresando al sistema
    (gmail de caracter informativo, no responder este gmail.)  {email_reciver}"""
    em = EmailMessage()
    em ["From"] = email_sender
    em ["To"] = email_reciver
    em ["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context() 
    with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context  ) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_reciver,em.as_string())  
    return

def recuperar(request):
    if request.method=='GET':
        return render(request,'recuperar.html')
    else: 
        usuario=User.objects.get(email=request.POST['correo']) 
        print(usuario.password)
        email() 
        return render(request,'recuperar.html',{
            'user':usuario.email
        })
    
@login_required
def desconectar(request):
    logout(request)
    return redirect('iniciarSesion')


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {'form': AuthenticationForm, 'error': 'el usuario o la contraseña  es incorrecto'})
        else:
            login(request, user)
            email(user.email)
            return redirect('home')
        
@login_required
def lista_productos(request):
    productos = Productos.objects.all()
    query = request.POST.get('q')
    if query:
        productos = productos.filter(nombre_producto__icontains=query)
    return render(request, 'lista_productos.html', {'productos': productos})
        

@login_required
def agregar_producto(request):
    if request.method == 'GET':
        return render(request, 'agregar_producto.html', {'form': producform})
    else:
        try:
            form = producform(request.POST)
            new_produc = form.save(commit=False)
            new_produc.save()
            return redirect('lista_productos')
        except ValueError:
            return render(request, 'agregar_producto.html', {"form": producform, "error": "Error creating producto."})
        
@login_required        
def editar_producto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=producto_id)
        Form = producform(instance=producto)
        return render(request, 'editar_producto.html', {'producto': producto, 'form': Form})
    else:
        try:
            producto = get_object_or_404(Productos,pk=producto_id)
            form = producform(request.POST, instance=producto)
            form.save()
            return redirect('lista_productos')
        except ValueError:
            return render(request, 'editar_producto.html', {'producto': producto, 'form': form, 'error': 'Error actualizando task.'})
        
@login_required
def eliminar_producto(request, producto_id):
    productos = get_object_or_404(Productos, pk=producto_id)
    if request.method == 'POST':
        productos.delete()
        return redirect('lista_productos')
    
@login_required
def clientess(request):
    cliente = clientes.objects.all()
    if request.method == 'GET':
        return render(request,'clientes.html',{'clientes':cliente})
    
@login_required
def agregar_cliente(request):
    if request.method == 'GET':
        return render(request, 'agregar_clientes.html', {'form': clientform})
    else:
        try:
            form = clientform(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'agregar_clientes.html', {"form": clientform, "error": "Error creating producto."})

@login_required
def borrar_clientes(request, clientes_id):
    clientess = get_object_or_404(clientes, pk=clientes_id)
    if request.method == 'GET':
        clientess.delete()
        return redirect('clientes')

@login_required
def editar_cliente(request, clientes_id):
    if request.method == 'GET':
        clientess = get_object_or_404(clientes, pk=clientes_id)
        Form = clientform(instance=clientess)
        return render(request, 'editar_clientes.html', {'clientes': clientess, 'form': Form})
    else:
        try:
            clientess = get_object_or_404(clientes,pk=clientes_id)
            form = clientform(request.POST, instance=clientess)
            form.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'editar_clientes.html', {'clientes': clientess, 'form': form, 'error': 'Error actualizando task.'})

@login_required
def lista_clientesss(request):
    clientess = clientes.objects.all()
    query = request.POST.get('q')
    if query:
        clientess = clientess.filter(cedula__icontains=query)
    return render(request, 'clientes.html', {'clientes': clientess})

@login_required
def carrito(request):
    if request.method=='GET':
        productos = Productos.objects.all()
        return render(request,'carrito.html',{'productos':productos})
    else:
        productos = Productos.objects.filter(nombre_producto__icontains=request.POST['nombre'])
        return render(request,'carrito.html',{'productos':productos})
    
@login_required        
def agregar_al_carrito(request):
    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            producto_id = request.POST['producto_id']
            cantidad = request.POST['cantidad']
            producto = Productos.objects.get(pk=producto_id)
            Carrito.objects.create(id_producto=producto,nomproducto=1,precio=2500,cantidad=cantidad)
            return redirect('carrito')
    else:
        productos = Productos.objects.all()
        form = AgregarAlCarritoForm()
    return render(request, 'carrito.html', {'form': form,'productos':productos})