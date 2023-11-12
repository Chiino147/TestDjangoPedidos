from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def logistica(request):
    
    contexto = {
        "querieStock": Stock.objects.all().order_by("stock") #Traemos el stock
    }
    return render(request,'mostrarStock.html', contexto)



def actualizarStock(request):
    nueva_cantidad = 0
    contexto={
        "querieStock": Stock.objects.all().order_by("stock"),
    }
    if request.method == "POST":
        nueva_cantidad = 0 #Para resetear la nueva cantidad
        for i in Stock.objects.all(): #Recorremos el stock
            nueva_cantidad = request.POST[str(i.cod_art)] # a travez de un post traemos la nueva partidad
            producto = Stock.objects.get(cod_art = i.cod_art) #agarramos el objeto que se va a actualizar
            producto.stock = nueva_cantidad #Hacemos el update
            producto.save() #Se salva
            contexto["alerta"]="Actualizo el stock!"
        return render(request,'mostrarStock.html', contexto)
    return render(request,'editarStock.html', contexto)





def mostrarPedidos(request):
    contexto = {
        "queriePedidos":Pedidos.objects.all()
    }
    if request.method == "POST":
        return render(request, 'mostrarPedido.html', contexto)
    return render(request, 'mostrarPedidos.html', contexto)


def verPedido(request, cod):
    contexto= {
        "queriePedidos":Pedidos.objects.all(),
        "codigo":cod,
        "queriePedido_detalle":Detalle_Pedidos.objects.filter(nro_pedido=cod),
    }
    array = () 
    pedido = {}
    if request.method == "POST":
        actualizarDetalle(request,cod,contexto)
        
        contexto["queriePedidos"]=Pedidos.objects.all()
        contexto["alerta"]= (f"Se cargo la cantidad entregada al  pedido {cod}")
        return render(request, 'mostrarPedidos.html', contexto)

            
    return render(request, 'mostrarPedido.html', contexto)


def actualizarDetalle(request,cod,contexto):
    for a in Detalle_Pedidos.objects.filter(nro_pedido=cod): #Filtro por pedido
            #Filtro por pedido + cod_art                                        Realizo el update
            new_cant = int(request.POST[a.cod_art.descripcion])
            resultado = 0
            resultado = a.cod_art.stock - new_cant
            if((resultado >= 0) & (not Remito.objects.get(nro_pedido = cod))):
                #print(f"Hay stock ya que hay {a.cod_art.stock} y quedaria {resultado}")
                Stock.objects.filter(cod_art = a.cod_art.cod_art, descripcion = a.cod_art.descripcion).update(stock=resultado)
                Detalle_Pedidos.objects.filter(nro_pedido=cod,cod_art=a.cod_art.cod_art).update(cant_entregada=request.POST[a.cod_art.descripcion])
            else:
                #print(f"No hay suficiente stock el resultado seria {resultado}")
                contexto["alerta"]=(f'No hay suficiente stock para el producto {a.cod_art.descripcion}')
            crearRemito(cod)
            return None 

def crearRemito(pedido):
    if not Remito.objects.filter(nro_pedido=pedido):
        Remito.objects.create(
            fecha= datetime.now(),
            c_total = Detalle_Pedidos.objects.filter(nro_pedido=pedido).count(),
            nro_pedido =  Pedidos.objects.get(nro_pedido=pedido),
            fecha_pedido = Pedidos.objects.get(nro_pedido=pedido).fecha
        )
    else:
        print("Ya hay un remito creado")
    
    
def buscadorPedidos(request):
    print("hHOLA")
    return render(request,'verPedido.html',{})