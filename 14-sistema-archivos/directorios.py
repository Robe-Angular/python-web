import os,shutil

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print('Ya existe el directorio')

#Eliminar una carpeta
#os.rmdir('./mi_carpeta')

"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"
shutil.copytree(ruta_original, ruta_nueva)
"""
"""
#Eliminar una carpeta
os.rmdir('./mi_carpeta_copiada')
"""
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print(f"Fichero: '{fichero}'")