from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.base, name='pedidoulrs'),
    path('eliminarProducto/<int:a>/', views.eliminarProducto, name="eliminarProducto"),
    path('editarProducto/<int:a>/', views.editarProducto, name="editarProducto"),
]