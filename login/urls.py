from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='a'),
    path('', views.login, name='login'),
]
