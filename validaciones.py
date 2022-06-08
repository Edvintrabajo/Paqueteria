import sys
from models.pedido import Pedido
from models.productos import Producto
sys.path.append('models') 
from models.table import Table
from models.pedido_producto import *

def validaciondni(dni): 

    if len(dni) != 9:
        return False

    if dni[8].isdigit():
        return False

    for numero in dni[:8]:
        if numero.isdigit() == False:
            return False

    return True

def asignarprecio_distancia(id_p):
    pedido = Pedido()
    distancia = pedido.get({"Distancia"}, id_p)
    distancia = distancia[0]

    if distancia >= 1 and distancia <= 25:
        precio_distancia = 5
    elif distancia >= 26 and distancia <= 50:
        precio_distancia = 10
    elif distancia >= 51 and distancia <= 15:
        precio_distancia = 15
    else:
        precio_distancia = 20

    pedido.update({"CosteTotal": precio_distancia}, id_p)

def asignarprecio(id_p_p):
    p_p = Pedido_Producto()
    pedido = Pedido()
    producto = Producto()

    id_pedido = p_p.get({"IDPedido"}, id_p_p)
    id_pedido = id_pedido[0]
    id_producto = p_p.get({"IDProducto"}, id_p_p)
    id_producto = id_producto[0]

    peso = producto.get({"PesoProducto"}, {"IDProducto" : id_producto})
    peso = peso[0]
    cantidad = producto.get({"CantidadProducto"}, {"IDProducto" : id_producto})
    cantidad = cantidad[0]
    precio = pedido.get({"CosteTotal"}, {"IDPedido" : id_pedido})
    precio = precio[0]
    peso_total = pedido.get({"PesoTotal"}, {"IDPedido" : id_pedido})
    coste_producto = peso * cantidad
    if peso_total != False or peso_total != None:
        peso_total = peso_total[0]

    if peso_total == None or peso_total == 0:
        peso_total = coste_producto
    else:
        peso_total += coste_producto

    precio += coste_producto

    pedido.update({"CosteTotal": precio}, {"IDPedido" : id_pedido})
    pedido.update({"PesoTotal": peso_total}, {"IDPedido" : id_pedido})

def eliminar_producto_en_pedido(id_p_p):
    p_p = Pedido_Producto()
    pedido = Pedido()
    producto = Producto()

    id_pedido = p_p.get({"IDPedido"}, id_p_p)
    id_pedido = id_pedido[0]
    id_producto = p_p.get({"IDProducto"}, id_p_p)
    id_producto = id_producto[0]

    peso = producto.get({"PesoProducto"}, {"IDProducto" : id_producto})
    peso = peso[0]
    precio = pedido.get({"CosteTotal"}, {"IDPedido" : id_pedido})
    precio = precio[0]
    peso_total = pedido.get({"PesoTotal"}, {"IDPedido" : id_pedido})
    peso_total = peso_total[0]
    cantidad = producto.get({"CantidadProducto"}, {"IDProducto" : id_producto})
    cantidad = cantidad[0]
    peso_producto = peso * cantidad

    peso_total -= peso_producto
    precio -= peso_producto

    pedido.update({"CosteTotal": precio}, {"IDPedido" : id_pedido})
    pedido.update({"PesoTotal": peso_total}, {"IDPedido" : id_pedido})