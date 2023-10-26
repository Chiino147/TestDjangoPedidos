from http.client import HTTPResponse
from django.shortcuts import render , redirect
from .forms import Formpedido
from .models import *
# Create your views here.

class Carrito():
    carro = {}
    def Carrito(self,art,cant):
        self.carro[art]=cant

    def getCarrito(self):
        return self.carro
    def eliminarProducto(self,produc):
        self.carro.pop(produc)

carrito = Carrito()


def base(request):
    formularioPedido = Formpedido()
    productos = Stock.objects.all()
    contexto = {
        "formulario":formularioPedido,
        "productos":productos,
    }


    if request.method == "POST":
        getcantidad = request.POST["Cantidades"]
        getcantidad = int(getcantidad)
        getproducto = request.POST["Productos"]
        getproducto = int(getproducto)
        carrito.Carrito(Stock.objects.filter(cod_art=getproducto).values_list("descripcion")[0][0],getcantidad)
        
        contexto["querie"]=carrito.getCarrito()
    if request.method == "GET":
        print("Entro al get")

    return render(request,"base.html",contexto)

def eliminarProducto(request, a): #Funcion que se encarga de borrar el producto
    productos = Stock.objects.all()
    contexto = {
    }
    carrito.eliminarProducto(a)
    contexto["querie"]=carrito.getCarrito()
    return render(request,"base.html",contexto)
    

