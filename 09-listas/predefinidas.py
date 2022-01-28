cantantes = ["2pac", "Drake", "Bad bunny", "Julio Iglesias"]
numeros = [1, 2, 5, 8, 3, 4]
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
print(cantantes)
cantantes.append("natos y waor")
cantantes.insert(1, "Davis Bisbal")
print(cantantes)

#eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove("Bad bunny")
print(cantantes)
#Dar la vuelta
numeros2=[1,23,43,3,3,7,9,10]
numeros2.sort(reverse = True)
numeros2.reverse()
print(numeros2)
#Buscar dentro de un lista
print("Drake" in cantantes)

#Contar elementos
print(cantantes)
print(len(cantantes))

#Cuántas veces aparece un elemento en la lista
numeros2.append(3)
print(numeros2.count(3))

print(numeros2.count(23))

#Conseguir índice
print(numeros2)
print(numeros2.index(3))
cantantes.extend(numeros2)
print(cantantes)
print(cantantes.index(3))