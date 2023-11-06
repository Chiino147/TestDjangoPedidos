# Generated by Django 4.2.5 on 2023-11-05 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('cod_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle_pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_pedida', models.IntegerField()),
                ('cod_art', models.ForeignKey(db_column='cod_art', on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
                ('pedido', models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.CASCADE, to='stock.pedido')),
            ],
            options={
                'db_table': 'detalle_pedido',
                'managed': True,
            },
        ),
    ]
