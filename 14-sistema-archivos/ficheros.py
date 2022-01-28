from io import open
import pathlib
import shutil

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo = open(ruta, "a+")

#Escribir dentro de un archivo
archivo.write('******* Soy un texto metido desde python :o *******\n')
archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo_lectura = open(ruta, "r")
#Leer contenido
#contenido = archivo_lectura.read()
print(archivo_lectura)

#print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)
print(archivo_lectura)

for elemento in lista:
    #lista_frase = elemento.split()
    #print(lista_frase)
    print(f"- {elemento.center(100)}")

#Compiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"
shutil.copyfile(ruta_original, ruta_nueva)
shutil.copyfile(ruta_original, ruta_alternativa)

#Mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado_nuevo.txt"
shutil.move(ruta_original, ruta_nueva)

#Remove

import os

os.remove(ruta_nueva)

import os.path
print(os.path.abspath("./"))

print(os.path.isfile(os.path.abspath("./") + "/fichero_texto22.txt"))
print(os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"))
