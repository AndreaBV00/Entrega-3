from django.db import models

# Create your models here.
class Cliente(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     telefono = models.CharField(max_length=9)
     email = models.EmailField()
     direccion = models.CharField(max_length=100)
 
      
class Producto(models.Model):
     nombre = models.CharField(max_length=50)
     precio = models.FloatField()
     descripcion = models.CharField(max_length=100)

class Pedido(models.Model):
     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
     fecha = models.DateField()
     total = models.FloatField()
     productos = models.ManyToManyField(Producto)
     