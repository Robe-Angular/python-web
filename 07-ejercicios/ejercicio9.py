"""
Ejercicio 9
    Hacer un programa que pida números al usuario
    hasta meter el número 111
"""
contador = 1
while contador < 111:
    numero = int(input('Introduce un numero: '))
    if numero == 111:
        print(f'Has introducido el {numero}')
        break
    else:
        print(f'Has introducido el {numero}')