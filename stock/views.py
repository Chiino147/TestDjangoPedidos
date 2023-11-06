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



def actualizarStock(request):
    nueva_cantidad = 0
    contexto={
        "querieStock": Stock.objects.all(),
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
        "queriePedidos":Pedido.objects.all()
    }
    if request.method == "POST":
        return render(request, 'mostrarPedido.html', contexto)
    return render(request, 'mostrarPedidos.html', contexto)

def verPedido(request, cod):
    
    contexto= {
        "queriePedidos":Pedido.objects.all(),
        "codigo":cod,
    }
    
    array = ()
    pedido = {}
    for p in Detalle_pedido.objects.filter(pedido_id=cod): #Cree una copia del carrito para obtener los productos
        #print(f"el coddigo es {p.cod_art} el  producto es {p.cod_art.descripcion} y se pidio {p.cant_pedida}")
        array =(p.cod_art.descripcion,p.cant_pedida,p.cant_entregada)
        pedido[p.cod_art.cod_art]=array
    contexto["queriePedido"]=pedido
    
    if request.method == "POST": #Cuando se carga el post
        for p in pedido:
           dp = Detalle_pedido.objects.get(pedido_id=cod,cod_art= p)
           dp.cant_entregada = request.POST[str(p)]
           dp.save()
           entregar = Pedido.objects.get(cod_pedido=cod)
           entregar.entregado = 1
           entregar.save()
        contexto["alerta"]="SE CARGO LA CANTIDAD ENTREGADA"

        return render(request, 'mostrarPedidos.html', contexto)


    return render(request, 'mostrarPedido.html', contexto)