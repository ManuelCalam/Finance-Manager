import sqlite3

connection = sqlite3.connect("finanzas.db")

try:
    connection.execute("""CREATE TABLE Fondos(Total DOUBLE PRIMARY KEY);
    """)
    print("La tabla Fondos se ha creado")
except sqlite3.OperationalError:
    print("La tabla Fondos ya existe")
connection.close()