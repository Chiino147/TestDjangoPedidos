from django.db import models

# Create your models here.

class Stock(models.Model): #Modelo del stock
    cod_art = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    stock = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'stock'

class Pedido(models.Model):   #Modelo para los pedidos
    cod_pedido = models.AutoField(primary_key=True)
    cod_detalle = models.IntegerField()
    usuario = models.CharField(max_length=50)
    #cod_art = models.ForeignKey(Stock, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'pedido'

class Usuario(models.Model):
    dni = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'usuario'

class Detalle_pedido(models.Model):
    id_detalle_ped = models.AutoField(primary_key=True)
    cod_art = models.IntegerField()
    cantidad = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'detalle_pedido'



