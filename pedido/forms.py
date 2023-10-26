from django import forms
from .models import *


class Formpedido(forms.Form):
    productos = Stock.objects.all()
    opciones = []
    tupla = ()
    for i in productos.values():
        tupla = (i["cod_art"],i["descripcion"])
        opciones.append(tupla)
    

    Cantidades = forms.IntegerField()
    Productos = forms.ChoiceField(choices=opciones)
