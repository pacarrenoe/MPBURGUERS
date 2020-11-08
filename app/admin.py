from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Producto, Cliente, Pedido

# Register your models here.


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido)
