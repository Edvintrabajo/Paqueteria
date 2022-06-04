import sys
sys.path.append('models') 
from models.pedido import Pedido
from validaciones import *
from models.pedido_producto import *
from config.create_database import create_database
from config.config import DATABASE

if __name__ == '__main__':
    create_database(DATABASE)

    list_id_p = Pedido().select_id("IDPedido")
    list_id_p_p = Pedido_Producto().select_id("ID_Pedido_Producto")

    for id2 in list_id_p:
        id2 = id2[0]
        asignarprecio_distancia({"IDPedido" : id2})

    for id in list_id_p_p:
        id = id[0]
        asignarprecio({"ID_Pedido_Producto" : id})