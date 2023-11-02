from django import forms
from .models import *


class Formeditarstock(forms.Form):
    productos = Stock.objects.all()
    opciones = []
    tupla = ()
    for i in productos.values():
        tupla = (i["cod_art"],i["descripcion"])
        opciones.append(tupla)
    

    Productos = forms.ChoiceField(choices=opciones)
    Cantidades = forms.IntegerField()