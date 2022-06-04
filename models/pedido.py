import sys
sys.path.append('models')
import sqlite3
from table import Table
from config.config import DATABASE

TABLE_NAME = 'Pedido'

class Pedido(Table):
    def __init__(self):
        self._table_name = TABLE_NAME
        self._db_name = DATABASE

    def select_maxid(self):
        rows = None
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(idpedido) FROM pedido")
            rows = cursor.fetchone()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
            return rows