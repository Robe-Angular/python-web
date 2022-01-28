import sqlite3

#Conexión a sqlite
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()



#Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255),"+
"descripcion text(255),"+
"precio int(255)"+
")")

#Guardar cambios
#conexion.commit()

"""
#Insertar datos
cursor.execute("INSERT INTO productos VALUES(null, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

#Borrar registros
cursor.execute("DELETE FROM productos")

#conexion.commit()


#Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", 'Buen PC', 700),
    ("Teléfono Móvil", 'Buen teléfono', 140),
    ("Placa base", 'Buena placa', 80),
    ("Tablet 15", 'Buen tablet', 300)
]

cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)


conexion.commit()

#Update 
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300")
productos = cursor.fetchall()
print(productos)

for producto in productos:
    print(f"ID:", producto[0])
    print(f"Nombre: {producto[1]}")
    print(f"Decripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print('\n')

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#Cerrar conexión
conexion.close()