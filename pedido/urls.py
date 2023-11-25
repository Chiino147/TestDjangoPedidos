from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.base, name='pedidoulrs'),
    path('tabla/', views.base, name='pedidoulrs'),
    path('eliminarProducto/<int:a>/', views.eliminarProducto, name="eliminarProducto"),
    path('editarProducto/<int:a>/', views.editarProducto, name="editarProducto"),
    path('finalizarPedido/', views.finalizarPedido, name='finalizarCarrito'),
    path('buscadorPedidos/', views.buscadorPedidos, name='buscadorPedidos'),
    path('tabla/',views.tablaProducto, name='tablaProductos'),
    path('stock/', include("stock.urls"),),
]