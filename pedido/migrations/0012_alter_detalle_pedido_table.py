# Generated by Django 4.2.5 on 2023-11-07 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0011_detalle_pedido_delete_detallepedido'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='detalle_pedido',
            table='detalle_pedido',
        ),
    ]