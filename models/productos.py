import sqlite3
from table import Table
from config import DATABASE

TABLE_NAME = 'Producto'

class Cliente(Table):
    def __init__(self):
        super().__init__(DATABASE)
        self._table_name = TABLE_NAME
