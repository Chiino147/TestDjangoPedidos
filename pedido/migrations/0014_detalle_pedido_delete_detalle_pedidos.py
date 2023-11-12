# Generated by Django 4.2.5 on 2023-11-07 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0013_detalle_pedidos_delete_detalle_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_pedido',
            fields=[
                ('pedido', models.OneToOneField(db_column='pedido', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pedido.pedido')),
                ('cant_pedida', models.FloatField()),
                ('cant_entregada', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalle_pedidos',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Detalle_pedidos',
        ),
    ]