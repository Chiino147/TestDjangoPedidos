from django.db import models

# Create your models here.

class Stock(models.Model):
    cod_art = models.IntegerField(primary_key=True,  db_column='cod_art')
    descripcion = models.CharField(max_length=50, blank=True, null=True,  db_column='descripcion')
    stock = models.IntegerField(blank=True, null=True,  db_column='stock')
    stock_min = models.IntegerField(blank=True, null=True,  db_column='stock_min')

    class Meta:
        managed = False
        db_table = 'stock'

class Detalle_Pedidos(models.Model):
    nro_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='nro_pedido',primary_key=True)
    cod_art = models.ForeignKey('Stock', models.DO_NOTHING, db_column='cod_art')
    cant_pedida = models.IntegerField()
    cant_entregada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedidos'
        unique_together = (('nro_pedido', 'cod_art'),)

class Pedidos(models.Model):
    nro_pedido = models.AutoField(primary_key=True,  db_column='nro_pedido')
    fecha = models.DateField(blank=True, db_column='fecha')
    solicitante = models.IntegerField(blank=True,   db_column='solicitante')
    entregado = models.IntegerField(blank=True,   db_column='entregado')

    class Meta:
        managed = False
        db_table = 'pedidos'

        


class Usuario(models.Model):
    cod_usuario = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True)
    apellido = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'usuario'

class Remito(models.Model):
    nro_remito = models.AutoField(primary_key=True, db_column='nro_remito')
    fecha = models.DateField(blank=True, null=True, db_column='fecha')
    fm_sol = models.CharField(max_length=50, blank=True, null=True, db_column='fm_sol')
    c_total = models.IntegerField(blank=True, null=True, db_column='c_total')
    nro_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='nro_pedido', blank=True, null=True)
    fecha_pedido = models.DateField(blank=True, null=True, db_column='fecha_pedido')

    class Meta:
        managed = False
        db_table = 'remito'


