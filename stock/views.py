from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def logistica(request):
    contexto = {
        "querieStock": Stock.objects.all() #Traemos el stock
    }
    return render(request,'mostrarStock.html', contexto)


def ActualizarStock(request): #Esta vista se encarga de actualizar el stock!
    contexto={
        'formEditar':Formeditarstock
    }
    if request.method == "POST": #Recibimos un post
        
        producto = request.POST["Productos"]
        cantidad = request.POST["Cantidades"]
        cantidad = int(cantidad)
        if(cantidad>=0):
            a = Stock.objects.get(cod_art=producto) #Filtramos por el id
            a.stock = cantidad  #Cambiamos su cantidad
            a.save()
            contexto["alerta"]="El producto se actualizo!"
        else:
            contexto["alerta"]="ERROR"
    return render(request, 'editarStock.html', contexto)

def mostrarPedidos(request):
    contexto = {
        "queriePedidos":Pedido.objects.all()
    }
    if request.method == "POST":
        return render(request, 'mostrarPedido.html', contexto)
    return render(request, 'mostrarPedidos.html', contexto)

def verPedido(request, cod_pedido):
    print(cod_pedido)
    contexto= {
        "queriePedido":cod_pedido
    }
    
    #a = Detalle_pedido.objects.all()
    #print(a.filter(cant_pedida=5))  Aca tira error ya (me encargare otro dia :P)

    return render(request, 'mostrarPedido.html', contexto)