from django.db import models

# Create your models here.
from django.db import models 

# Create your models here.

class Producto (models.Model):
    CodigoP=models.AutoField(primary_key=True, verbose_name="Codigo -")
    NombreP=models.CharField(max_length=35, verbose_name="Nombre del producto -")
    PrecioP=models.IntegerField(verbose_name="Precio -")
    Descripcion=models.TextField(max_length=500, blank=True, null=True, verbose_name="Descripcion -")
    Imagen=models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.NombreP


class Cliente (models.Model):   
    RutC=models.AutoField(primary_key=True, verbose_name="Rut -")
    Nombres=models.CharField(max_length=70, verbose_name="Nombre ")
    Apellidos=models.CharField(max_length=70, verbose_name="Apellido -")
    Direccion=models.CharField(max_length=70, verbose_name="Direccion -")
    Fono=models.IntegerField( verbose_name="Numero contacto -")
    Email=models.EmailField(blank=True, null=True, verbose_name="Email -")    
    
    def DatosCliente(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.Nombres, self.Apellidos, self.Fono)

    def __str__ (self):
        return self.DatosCliente()    

class Pedido (models.Model): 
    NumPedido=models.AutoField(primary_key=True, verbose_name="Numero de pedido -")
    Cliente=models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Cliente -")
    Producto=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Producto -")
    Estado=models.BooleanField(verbose_name="Estado -")
    Fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de pedido -")

    def Final(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.Cliente, self.NumPedido, self.Estado)

    def __str__ (self):
        return self.Final()    
                          
                      
