#Ejemplo 1
print('###Ejemplo1###')

def muestraNombre():
    print("Víctor")
    print("Raúl")
    print("Paco")
    print("Francisco")
    print("Néstor")
    print("\n")
    print("####Adiós####")

muestraNombre()
muestraNombre()

#Ejemplo 2
print('####Ejemplo 2 ####')
def mostrarTuNombre(nombre = 'Cristian', edad = 17):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

mostrarTuNombre('Víctor Robles', 20)
mostrarTuNombre('Paquito', 30)
mostrarTuNombre('JuanFran', 90)
mostrarTuNombre()

"""
nombre = input('Introduce tu nombre: ')
mostrarTuNombre(nombre)
edad = int(input('Introduce tu edad: '))
mostrarTuNombre(nombre, edad)
"""
def tabla(numero = 1):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f'{numero} x {contador} = {operacion}')

    print("\n")
tabla()
tabla(2)
"""
numero_introducido = int(input('Introduce el número para sacar la tabla'))
tabla(numero_introducido)
"""
"""
print('-------------------------------------')
"""

for numero_tabla in range(1,11):
    tabla(numero_tabla)
#Devolver Datos de una función
print('####Devolver datos de una función####')

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo
print(saludame("Víctor Robles"))

#Calculadora
print('\n####Calculadora####')
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
    return(cadena)

print(calculadora(5,2,False))
#Ejemplo 7
print('\n####Ejemplo número 7####')

def getNombre(nombre):
    texto = f'El nombre es: {nombre}'
    return texto

def getApellidos(apellidos):
    texto = f'Los apellidos son: {apellidos}'
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo('Roberto', 'De la Cruz'))

#Ejemplo 8
print('\n####Función lambda Ejemplo 8####')
dime_el_year = lambda year, nombre: f"{nombre} El año es {year * 5}"
print(dime_el_year(2034, 'Robe'))

