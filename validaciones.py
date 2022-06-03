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

def asignarprecio(id_p_p):
    p_p = Pedido_Producto()
    pedido = Pedido()
    producto = Producto()

    id_pedido = p_p.get({"IDPedido"}, id_p_p)
    id_producto = p_p.get({"IDProducto"}, id_p_p)

    peso = producto.get({"PesoProducto"}, {"IDProducto" : list(id_producto)[0]})
    cantidad = producto.get({"CantidadProducto"}, {"IDProducto" : list(id_producto)[0]})
    distancia = pedido.get({"Distancia"}, {"IDPedido" : list(id_pedido)[0]})
    precio = pedido.get({"CosteTotal"}, {"IDPedido" : list(id_pedido)[0]})
    peso_total = pedido.get({"PesoTotal"}, {"IDPedido" : list(id_pedido)[0]})
    precio_distancia = 0

    cantidad = list(cantidad)[0]
    precio = list(precio)[0]
    peso = list(peso)[0]
    peso_total = list(peso_total)[0]
    
    if peso_total == None:
        peso_total = peso
    else:
        peso_total += peso
    
    if precio == None:
        precio = 0


    if list(distancia)[0] >= 1 or list(distancia)[0]<= 25:
        precio_distancia = 5
    elif list(distancia)[0]>= 26 or list(distancia)[0]<= 50:
        precio_distancia = 10
    elif list(distancia)[0]>= 51 or list(distancia)[0]<= 15:
        precio_distancia = 15
    else:
        precio_distancia = 20

    precio += (peso_total * cantidad) + precio_distancia

    pedido.update({"CosteTotal": precio}, {"IDPedido" : list(id_pedido)[0]})
    pedido.update({"PesoTotal": peso_total}, {"IDPedido" : list(id_pedido)[0]})


