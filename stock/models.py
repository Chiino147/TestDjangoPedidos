from django.db import models

# Create your models here.
class Stock(models.Model):
    cod_art = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    stock_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'

class Pedidos(models.Model):
    nro_pedido = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    solicitante = models.IntegerField(blank=True, null=True)
    entregado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'

        
class Detalle_Pedidos(models.Model):
    nro_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='nro_pedido',primary_key=True)
    cod_art = models.ForeignKey('Stock', models.DO_NOTHING, db_column='cod_art')
    cant_pedida = models.IntegerField()
    cant_entregada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedidos'
        unique_together = (('nro_pedido', 'cod_art'),)

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