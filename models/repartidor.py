import sqlite3

class Producto:
    def __init__(self, database):
        self.database = database
    
    def __connect(self):
        conn = sqlite3.connect(self.database)
        return conn

    def select_repartidor(self):
        data = None
        try:
            conn = self.__connect()
            c = conn.cursor()
            c.execute("SELECT * FROM Repartidor")
            data = c.fetchall() # Cursor
            conn.commit()
            c.close()
        except sqlite3.Error as error:
            print("No se ha podido mostar los Repartidores", error)

        finally:
            if conn:
                conn.close()
            return data

if __name__ == "__main__": 
    all =  Producto("paqueteria.db")
    print(all.select_repartidor())