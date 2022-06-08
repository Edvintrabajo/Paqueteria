import sqlite3
import sys
sys.path.append('models')
from models.table import Table
from config.config import DATABASE

TABLE_NAME = 'Pedido_Producto'

class Pedido_Producto(Table):
    def __init__(self):
        self._table_name = TABLE_NAME
        self._db_name = DATABASE
