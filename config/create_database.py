import sqlite3
def create_database(db_file):
    conn = sqlite3.connect(db_file) # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE Cliente (DNIcliente char(9) PRIMARY KEY, Nombre char(30) NOT NULL, Apellidos char(30) NOT NULL, DireccionCliente char(50) NOT NULL)")
    conn.execute("INSERT INTO Cliente (DNIcliente, Nombre, Apellidos, DireccionCliente) VALUES ('12345678A', 'Carlos', 'Freyer', 'Las Palmas')")
    conn.execute("INSERT INTO Cliente (DNIcliente, Nombre, Apellidos, DireccionCliente) VALUES ('12345678B', 'Mario', 'Alonso', 'Telde')")
    conn.execute("INSERT INTO Cliente (DNIcliente, Nombre, Apellidos, DireccionCliente) VALUES ('12345678C', 'Richard', 'Ramirez', 'Galdar')")
    conn.commit()