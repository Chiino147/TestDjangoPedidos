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
    user= models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'pedido'
        
class Detalle_pedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, db_column="pedido_id", on_delete= models.CASCADE)
    cod_art = models.IntegerField()
    cant_pedida = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'detalle_pedido'

class Usuario(models.Model):
    dni = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'usuario'




