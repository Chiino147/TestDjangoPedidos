from http.client import HTTPResponse
from django.shortcuts import render , redirect
from .forms import *
from .models import *

# Carrito linea 7

# vista Base linea 35

# Vista eliminarProducto linea 67

# Vista editarProducto linea 72





#Este el carrito
class Carrito():
    carro = {}
    def Carrito(self,cod_art,art,cant):
        orden = [art,cant]
        self.carro[cod_art]=orden
        #Se guarda de la siguiente manera carro = {1:["Lapicera roja",1], 2:["Carpeta Veloz", 5] }

    def getCarrito(self): #Retornamos el carro
        return self.carro
    
    def getOrden(self,cod_art): #Retornamos el array  (osea el valor del la key)
        return self.carro[cod_art]
    def getKeys(self):
        keys = self.carro.keys()
        akeys = []
        for i in keys:
            akeys.append(i)
        return akeys
        
        
    
    def eliminarProducto(self,cod_art): 
        self.carro.pop(cod_art)

   
    def editarCarrito(self,cod_art,cantidad): #Editar el carrito
        self.carro[cod_art][1] = cantidad
        print(self.carro)

carrito = Carrito()



def base(request):
    
    formularioPedido = Formpedido() #LLamamos al form para hacer los pedidos
    productos = Stock.objects.all() #Traemos todos los productos del modelo Stock
   
    contexto = {
        "formulario":formularioPedido,
        "productos":productos,
    }
    
    if request.method == "POST": #Si recibimos un POST vamos a guardar los datos 
        getcantidad = request.POST["Cantidades"]
        getcantidad = int(getcantidad)
        getproducto = request.POST["Productos"]
        getproducto = int(getproducto)

        carrito.Carrito(getproducto,Stock.objects.filter(cod_art=getproducto).values_list("descripcion")[0][0],getcantidad)
        
        contexto["querie"]=carrito.getCarrito() #Le enviamos todo nuestro carro al HTML para que lo cargue en una tabla
        return render(request,"mostrarTablaProductos.html",contexto)

    return render(request,"base.html",contexto)


def eliminarProducto(request, a): #Funcion que se encarga de borrar el producto
    formularioPedido = Formpedido()
    contexto = {
        "formulario":formularioPedido,
        "mensaje":"SE ELIMINO EL PRODUCTO!"
    }
    carrito.eliminarProducto(a) #Aca llamamos a la funcion para eliminar
    #print(carrito.getCarrito())
    contexto["querie"]=carrito.getCarrito()  #Le enviamos todo nuestro carro al HTML para que lo cargue en una tabla
    return render(request,"mostrarTablaProductos.html",contexto)


def editarProducto(request,a): #FUNCION PARA MODIFICAR
    formularioEditar = FormEditPedido() # Este formulario se encarga de editar 
    formularioPedido = Formpedido() # Este formulario es para crear nuevos pedidos (SE LO PASO POR ACA PORQUE SINO LA TEMPLATE NO LO CARGA)
    contexto = {
        "formulario":formularioPedido,
        "formularioEditar":formularioEditar,
        "querie":carrito.getCarrito(),
    }
    if request.method == "GET": #Enviamos el id por URL  y obtenemos la orden
        contexto['orden']= carrito.getOrden(a)
    elif request.method == "POST":  #Este POST es para realizar el guardado del edit
        newCant = request.POST["getCant"]
        carrito.editarCarrito(a,newCant)
        contexto["mensaje"]="SE EDITO EL PRODUCTO!"
        return render(request,"mostrarTablaProductos.html",contexto)

    return render(request,"editarCarrito.html",contexto)


def finalizarPedido(request):
    contexto={}
    keys = carrito.getKeys()
    #print(keys)
    carro = carrito.getCarrito()
    

    #Stock.objects.get(cod_art=1)
    fk = Stock.objects.get(cod_art = 1)
    #cod_art_id = Stock.objects.get(cod_art = 1,descripcion="Lapicera Roja",stock=17)
    a = Stock.objects.get(cod_art=1)
    print(a.cod_art)
    print(Pedido.objects.last())
    #Pedido.objects.create(cod_art=4,cod_usuario=1)
    for a,b in carro.items():
       print(f'Cod_art={a} producto= {b[0]} cantidad pedida = {b[1]}') #Cod_art=1 producto= Lapicera Roja cantidad pedida = 3
      
        
        #variable.save
    #querie = Pedido.objects()
    #contexto["querie"]=carrito.getCarrito()
   
    return render(request,"mostrarTablaProductos.html",contexto)


