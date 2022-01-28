"""
Ejercicio3
    Escribir programa que imprima los cuadrados de los primeros 
    60 números naturales. Resolver con for y con while
"""
i = 1
while i <= 60:
    print(f'{i} x {i} = {i * i}')
    i += 1
for i in range(1,61):
    print(f'El cuadrado de {i} es: {i * i}')

