import sqlite3
def create_database(db_file):
    conn = sqlite3.connect(db_file) Warning: This file is created in the current directory
   

    conn.execute('''CREATE TABLE IF NOT EXISTS 'Producto' (
        'IDProducto' INTEGER PRIMARY KEY AUTOINCREMENT, 
        'NombreProducto' VARCHAR(30) NOT NULL, 
        'CantidadProducto' INT NOT NULL CHECK(CantidadProducto>0), 
        'PesoProducto' DEC(4 , 2) NOT NULL CHECK(PesoProducto>0))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Cliente" (
	"DNIcliente"	VARCHAR(9),
	"Nombre"	VARCHAR(30) NOT NULL,
	"Apellidos"	VARCHAR(30) NOT NULL,
	"DireccionCliente"	VARCHAR(50) NOT NULL,
	PRIMARY KEY("DNIcliente"))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Oficinista" (
	"ID_Oficinista"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Nombre"	VARCHAR(30) NOT NULL)''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Repartidor" (
	"DNIRepartidor"	VARCHAR(9),
	"NombreRepartidor"	VARCHAR(30) NOT NULL,
	PRIMARY KEY("DNIRepartidor"))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Pedido" (
	"IDPedido"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"PesoTotal"	DEC(5 , 2),
	"CosteTotal"	DEC(6 , 2),
	"Distancia"	INTEGER NOT NULL CHECK(Distancia>0),
	"DireccionEnvio"	VARCHAR(50) NOT NULL,
	"Estado"	TEXT NOT NULL DEFAULT 'A' CHECK(Estado IN ('A','S','E','I')),
	"DNIRepartidor"	VARCHAR(9) NOT NULL,
	"DNIcliente"	VARCHAR(9) NOT NULL,
	FOREIGN KEY("DNIRepartidor") REFERENCES "Repartidor"("DNIRepartidor"),
	FOREIGN KEY("DNIcliente") REFERENCES "Cliente"("DNIcliente"))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Oficinista_Pedido" (
	"ID_Oficinista"	INTEGER,
	"IDPedido"	INTEGER,
	FOREIGN KEY("ID_Oficinista") REFERENCES "Oficinista"("ID_Oficinista"),
	FOREIGN KEY("IDPedido") REFERENCES "Pedido"("IDPedido"),
	PRIMARY KEY("IDPedido"))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Pedido_Producto" (
	"ID_Pedido_Producto"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"IDPedido"	INTEGER,
	"IDProducto"	INTEGER,
	FOREIGN KEY("IDProducto") REFERENCES "Producto"("IDProducto"),
	FOREIGN KEY("IDPedido") REFERENCES "Pedido"("IDPedido"))''')







    # conn.execute("""INSERT INTO Cliente (DNIcliente, Nombre, Apellidos, DireccionCliente) VALUES 
    # ('12345678A', 'Carlos', 'Freyer', 'Las Palmas'),
    # ('12345678B', 'Mario', 'Alonso', 'Telde'),
    # ('12345678C', 'Richard', 'Ramirez', 'Galdar')""")
    
    
    # conn.execute("CREATE TABLE Oficinista (ID_Oficinista INTEGER PRIMARY KEY AUTOINCREMENT, Nombre char(30) NOT NULL)")
    # conn.execute("INSERT INTO Oficinista (Nombre) VALUES ('Javi')")
    # conn.execute("INSERT INTO Oficinista (Nombre) VALUES ('Antonio')")
    # conn.execute("INSERT INTO Oficinista (Nombre) VALUES ('Pepe')")

    # conn.execute("CREATE TABLE Repartidor (DNIRepartidor char(9) PRIMARY KEY, NombreRepartidor char(30) NOT NULL)")
    # conn.execute("INSERT INTO Repartidor (DNIRepartidor, NombreRepartidor) VALUES ('12345678D', 'Carlos')")
    # conn.execute("INSERT INTO Repartidor (DNIRepartidor, NombreRepartidor) VALUES ('12345678E', 'Jose')")
    # conn.execute("INSERT INTO Repartidor (DNIRepartidor, NombreRepartidor) VALUES ('12345678F', 'Sara')")

    # conn.execute("CREATE TABLE Pedido (IDPedido INTEGER PRIMARY KEY AUTOINCREMENT, PesoTotal DEC(5,2) NULL, CosteTotal DEC(6,2) NULL, Distancia INTEGER NOT NULL CHECK(Distancia > 0), DireccionEnvio char(50) NOT NULL, Estado ENUM ('A','S','E','I') NOT NULL DEFAULT 'A', DNIRepartidor char(9) NOT NULL, DNIcliente char (9) NOT NULL)")
    # conn.execute("INSERT INTO Pedido (Distancia, DireccionEnvio, Estado, DNIRepartidor, DNIcliente) VALUES (40, 'Calle Diamante', 'A', '12345678D', '12345678B')")
    # conn.execute("INSERT INTO Pedido (Distancia, DireccionEnvio, Estado, DNIRepartidor, DNIcliente) VALUES (100, 'Calle Vulcano', 'A', '12345678E', '12345678A')")
    # conn.execute("INSERT INTO Pedido (Distancia, DireccionEnvio, Estado, DNIRepartidor, DNIcliente) VALUES (140, 'Calle Argentina', 'A', '12345678E', '12345678C')")
    # conn.execute("INSERT INTO Pedido (Distancia, DireccionEnvio, Estado, DNIRepartidor, DNIcliente) VALUES (80, 'Calle Las Canteras', 'A', '12345678D', '12345678A')")

    # conn.execute("CREATE TABLE Producto (IDProducto INTEGER PRIMARY KEY AUTOINCREMENT, NombreProducto VARCHAR(30) NOT NULL, CantidadProducto INTEGER NOT NULL CHECK(CantidadProducto > 0), PesoProducto DEC(4,2) NOT NULL CHECK(PesoProducto > 0))")
    # conn.execute("INSERT INTO Producto (NombreProducto, CantidadProducto, PesoProducto) VALUES ('Goma', 5, 0.10)")
    # conn.execute("INSERT INTO Producto (NombreProducto, CantidadProducto, PesoProducto) VALUES ('Frigorifico', 1, 40.00)")
    # conn.execute("INSERT INTO Producto (NombreProducto, CantidadProducto, PesoProducto) VALUES ('Sillon', 2, 50.00))")
    # conn.execute("INSERT INTO Producto (NombreProducto, CantidadProducto, PesoProducto) VALUES ('Tele', 1, 4.00)")


    conn.commit()
