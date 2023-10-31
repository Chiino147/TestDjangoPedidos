from django.urls import path, include

from . import views

urlpatterns = [
    path('logistica/', views.logistica, name='verStock'),
    
]