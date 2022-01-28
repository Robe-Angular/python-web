"""
#FOR
for variable in elemento_iterable(lista, rango. etc):
    Bloque de instrucciones
"""
resultado = 0
for contador in range(5,10):
    print(f'Voy en el {contador}')
    resultado += contador
print(f'El resultado es: {resultado}')

#Ejemplo tablas de multiplicar
print("\n#### Ejemplo ####")

numero = int(input('¿De qué numero quieres ver la tabla?'))
if numero < 1:
    numero =1

print(f"#### Tabla de multiplicar del número {numero} ####")

for numero_tabla in range(1,11):
    if numero == 45:
        print('No se pueden mostrar numeros prohibidos')
        break
    print(f"{numero} x {numero_tabla} = {numero_tabla * numero}")

else:
    print(f"Tabla del {numero} finalizado") 


