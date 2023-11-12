# Generated by Django 4.2.5 on 2023-11-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0015_alter_detalle_pedido_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_pedida', models.IntegerField()),
                ('cant_entregada', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalle_pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('nro_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('solicitante', models.IntegerField(blank=True, null=True)),
                ('entregado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Detalle_pedido',
        ),
        migrations.DeleteModel(
            name='pedido',
        ),
    ]