from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.logistica, name='verStock'),
    path('actualizar/', views.ActualizarStock, name='actualizarStock'),
    path('pedidos/', views.mostrarPedidos, name="mostrarPedidos"),
    path('verpedido/<int:cod_pedido>/', views.verPedido, name="verPedido"),
    
]