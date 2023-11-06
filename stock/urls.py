from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.logistica, name='verStock'),
    path('actualizar/', views.actualizarStock, name='actualizarStock'),
    path('pedidos/', views.mostrarPedidos, name="mostrarPedidos"),
    path('verpedido/<int:cod>/', views.verPedido, name="verPedido"),
    
]