"""
Listas (array)
Son colecciones o conjuntos de datos/valores,
bajo un único nombre. 
Para acceder a esos valores podemos usar un
índice numérico
"""
pelicula = "Batman"
peliculas=["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'drake', 'Jennifer Lopez'))
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4, True, "texto"]

"""
print(cantantes)
print(type(cantantes))
print(years)
print(variada)
"""
#Indices
peliculas[1] = 'Azul'
print(peliculas[1])
print(type(peliculas[-3]))
print(cantantes[0:1])
print(cantantes[2:])

#Añadir elementos a lista

cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes[2:])

#recorrer lista
"""
print("***********Listado Películas***********")

nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input('Introduce la nueva película: ')
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}.{pelicula}")

print(peliculas.index(peliculas[2]))
"""
#Listas multidimensionales
print("\n *********** Listado de contactos ***********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Email: {elemento}")
    print("\n")


print(contactos[1][1])