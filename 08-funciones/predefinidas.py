nombre = "Víctor Robles"
print(type(nombre))

#Detectar el tipado

comprobar = isinstance(nombre,bool)
print(comprobar)

#Limpiar espacios
frase = "   Mi contenido   "
print(frase.strip())

#Eliminar variables
year = 2022
print(year)
del year
#print(year)

#comprobar variable vacía
texto = "  ff   "
print(len(texto))

#encontrar caracteres dentro de un string

frase = "La vida es bella"
print(frase.find('es'))

nueva_frase = frase.replace('vida','casa')
print(nueva_frase)

print(nombre.upper())
print(nombre.lower())