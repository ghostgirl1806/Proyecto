from django.contrib import admin
from .models import Productos,clientes,Carrito

class taksAdmin( admin.ModelAdmin):
    readonly_fields = ("created",)
class proAdmin(admin.ModelAdmin):
    readonly_fields =("fecha_de_creacion",)
# Register your models here.
admin.site.register(Productos)
admin.site.register(clientes)
admin.site.register(Carrito)
