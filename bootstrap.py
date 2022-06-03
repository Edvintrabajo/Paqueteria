import sys
from models.pedido import Pedido
from models.productos import Producto
from validaciones import asignarprecio
sys.path.append('models') 
from models.table import Table
from models.pedido_producto import *
from config.create_database import create_database
from config.config import DATABASE

if __name__ == '__main__':
    create_database(DATABASE)

    list_id = Pedido_Producto().select_id("ID_Pedido_Producto")


    for id in list_id:
        id = list(id)[0]
        asignarprecio({"ID_Pedido_Producto" : id})