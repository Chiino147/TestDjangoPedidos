from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.base, name='pedidoulrs'),
    path('eliminarProducto/<str:a>/', views.eliminarProducto, name="eliminarProducto"),
]