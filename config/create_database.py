import sqlite3
def create_database(db_file):
    conn = sqlite3.connect(db_file)
   
   
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
	"PesoTotal" DEC(5 , 2) DEFAULT 0,
	"CosteTotal"	DEC(6 , 2) DEFAULT 0,
	"Distancia"	INTEGER NOT NULL CHECK(Distancia>0),
	"DireccionEnvio"	VARCHAR(50) NOT NULL,
	"Estado"	TEXT NOT NULL DEFAULT 'A' CHECK(Estado IN ('A','S','E','I')),
	"DNIRepartidor"	VARCHAR(9) NOT NULL,
	"DNIcliente"	VARCHAR(9) NOT NULL,
	FOREIGN KEY("DNIRepartidor") REFERENCES "Repartidor"("DNIRepartidor") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("DNIcliente") REFERENCES "ClieDEFAULT 0nte"("DNIcliente") ON UPDATE CASCADE ON DELETE CASCADE)''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Oficinista_Pedido" (
	"IDPedido"	INTEGER,
    "ID_Oficinista"	INTEGER,
	FOREIGN KEY("ID_Oficinista") REFERENCES "Oficinista"("ID_Oficinista") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("IDPedido") REFERENCES "Pedido"("IDPedido") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("IDPedido"))''')

    conn.execute('''CREATE TABLE IF NOT EXISTS "Pedido_Producto" (
	"ID_Pedido_Producto"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"IDPedido"	INTEGER,
	"IDProducto"	INTEGER,
	FOREIGN KEY("IDProducto") REFERENCES "Producto"("IDProducto") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("IDPedido") REFERENCES "Pedido"("IDPedido") ON UPDATE CASCADE ON DELETE CASCADE)''')

    conn.execute("""INSERT INTO Cliente (DNIcliente, Nombre, Apellidos, DireccionCliente) VALUES 
    ('12345678A', 'Carlos', 'Freyer', 'Las Palmas'),
    ('12345678B', 'Mario', 'Alonso', 'Telde'),
    ('12345678C', 'Richard', 'Ramirez', 'Galdar')""")

    conn.execute("""INSERT INTO "Oficinista" ("ID_Oficinista","Nombre") VALUES (1,'Javi'),
    (2,'Antonio'),
    (3,'Pepe')""")
    
    conn.execute("""INSERT INTO "Repartidor" ("DNIRepartidor","NombreRepartidor") VALUES ('12345678D','Carlos'),
    ('12345678E','Jose'),
    ('12345678F','Sara')""")

    conn.execute("""INSERT INTO "Producto" ("IDProducto","NombreProducto","CantidadProducto","PesoProducto") VALUES (1,'Goma',5,0.1),
    (2,'Frigorifico',1,40),
    (3,'Sillon',2,50),
    (4,'Tele',1,4)""")

    conn.execute("""INSERT INTO "Pedido" ("IDPedido","Distancia","DireccionEnvio","Estado","DNIRepartidor","DNIcliente") VALUES (1,40,'Calle Diamante','A','12345678D','12345678B'),
    (2,100,'Calle Vulcano','A','12345678E','12345678A'),
    (3,140,'Calle Argentina','A','12345678E','12345678C'),
    (4,80,'Calle Las Canteras','A','12345678D','12345678A')""")

    conn.execute("""INSERT INTO "Oficinista_Pedido" ("IDPedido", "ID_Oficinista") VALUES (1,1),
    (2,2),
    (3,3)""")

    conn.execute("""INSERT INTO "Pedido_Producto" ("ID_Pedido_Producto","IDPedido","IDProducto") VALUES (1,1,1),
    (2,1,2),
    (3,2,3),
    (4,2,4)""")

    conn.execute('''CREATE TABLE IF NOT EXISTS 'EdicionPedido'(
        'Numero_de_pedido' VARCHAR(50),
        'fecha' DATE)''')

    conn.execute("""CREATE TRIGGER actualizar_pedido
    AFTER UPDATE ON Pedido
    FOR EACH ROW
    BEGIN

        INSERT INTO EdicionPedido VALUES (NEW.IDPedido, CURRENT_DATE);

    END;""")

    conn.commit()
