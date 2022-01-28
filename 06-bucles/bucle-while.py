"""
# Bucle While
Estructura de control que itera o repite la ejecución
 de una serie de instrucciones tantas vece como sea 
 necesario hasta que se deje de cumplir la condición

 while condición:
     bloque de instrucciones
     actualización de contador
"""
contador = 1
muestrame = str(0)
while contador <= 100:
    print(f"Estoy en el número: {contador}")
    muestrame += ',' + str(contador)
    contador += 1
print('---------------------------------')
print(muestrame)
print('---------------------------------')
print("####Ejemplo####")
numero_usuario = int(input("¿De qué número quieres la tabla? "))
if numero_usuario < 1:
    numero_usuario = 1
    
print('--------INICIO--------')

print(f"### Tabla del {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print('--------FIN--------')