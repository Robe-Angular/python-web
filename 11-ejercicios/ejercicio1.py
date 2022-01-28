"""
Ejercicio 1. Hacer un programa que tenga uma lista
de 8 números enteros y haga lo siguiente:

-Recorrer una lista y mostrarla
-Hacer una función que recorra listas de números y devuelva un string
-ordenarla y mostrarla
-Mostrar su longitud
-Buscar algún elemento(que el usuario pida por el teclado)
"""

#Crear una lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

#Crear una función que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += str(f'El número es: {elemento}')
        resultado += '\n'
    return resultado

#Recorrer y mostrar
print("##### Recorrer y Mostrar #####")

for numero in numeros:
    print(numero)

print(mostrarLista(numeros))
print(mostrarLista(['numeros', 'letras']))

#Ordenar y mostrar
print("##### Ordenar y Mostrar #####")
numeros.sort(reverse=True)
print(mostrarLista(numeros))

#Mostrar su longitud
print("##### Mostrar su longitud #####")
print(len(numeros))
"""
#Búsqueda en la lista
print("##### Búsqueda en la lista #####")
try:
    busqueda = int(input("Introduce el número: "))
    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")

    print("##### Búsqueda en la lista #####")

    search = numeros.index(busqueda)
    print(f'El número buscado existe en la lista, es el indice: {search}')
except:
    print("El número no está en la lista, lo siento")
    """

#Múltiples excepciones
try:

    numero = int(input("Número para elevarlo al cuadrado: "))
    #numero = input("Número para elevarlo al cuadrado: ")
    print(f'El cuadrado es: {numero * numero}')
except TypeError:
    print('Debes convertir tus cadenas a enteros')
#except ValueError:
#    print('Introduce un número correcto')
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")

