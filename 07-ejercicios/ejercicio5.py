"""
ejercicio5
Imprimir todos los números entre dos numeros que diga el usuario
"""

numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))
if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        print(i)
else:
    print('El rango no es correcto')