import sqlite3
from table import Table
from config.config import DATABASE

TABLE_NAME = 'Producto'

class Pedido(Table):
    def __init__(self):
        self._table_name = TABLE_NAME
        self._db_name = DATABASE
