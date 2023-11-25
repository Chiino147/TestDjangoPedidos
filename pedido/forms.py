from django import forms
from .models import *


class Formpedido(forms.Form):
    productos = Stock.objects.all().order_by('descripcion')
    opciones = []
    tupla = ()
    for i in productos.values():
        tupla = (i["cod_art"],i["descripcion"])
        opciones.append(tupla)
    

    Productos = forms.ChoiceField(choices=opciones)
    Cantidades = forms.IntegerField()

class FormEditPedido(forms.Form):
    Cantidades = forms.IntegerField()