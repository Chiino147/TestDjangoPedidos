from django.db import models

# Create your models here.

class Stock(models.Model):
    cod_art = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    stock = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'stock'

class Pedido(models.Model):
    cod_pedido = models.IntegerField(primary_key=True)
    cod_usuario = models.IntegerField()
    cod_articulo = models.ForeignKey(Stock, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'pedido'