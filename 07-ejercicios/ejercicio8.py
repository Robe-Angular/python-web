"""
Ejercicio 8
    Sacar un programa que saque un porcentaje
    introducido por el usuario de un número
    también introducido
"""
numero_completo = int(input('Introduce el primer número: '))
porcentaje = int(input('Introduce el porcentaje: '))
print(f'El {porcentaje}% de {numero_completo} es: {(porcentaje / 100) * numero_completo}')