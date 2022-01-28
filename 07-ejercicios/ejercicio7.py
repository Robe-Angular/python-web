"""
Ejercicio 7
Hacer un programa que muestre
 todos los números impares entre
  dos números que decida el usuario
"""
numero1 = int(input('Introduce el primer número: '))
numero2 = int(input('Introduce el segundo número: '))

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        if i % 2 > 0:
            print(f'El número {i} es impar')
else:
    print('El primer número al segundo número')

