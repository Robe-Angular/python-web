"""
Ejercicio2.
    Escribir un programa que añada valores a una lista
    mientras que su longitud sea menor a 120 y luego
    mostrar la lista
"""
coleccion = []

"""

for contador in range(0,120):
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el: " + coleccion[contador])
print(coleccion[115])
"""
x=0

while x < 120:
    coleccion.append(f'elemento - {x}')
    print(f"Mostrando el {coleccion[x]}")
    x += 1
print(coleccion)