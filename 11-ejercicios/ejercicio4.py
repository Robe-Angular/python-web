"""
Ejercicio 4. 
    Crear un script que tenga 4 variables, una lista, un string,
    un entero un booleano, que imprima un mensaje según el tipo 
    de dato de cada variable

"""
def traducir(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Integer"
    else:
        result = "Boolean"
    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        result= f"Este dato es del tipo {traducir(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result
    


mi_lista=["hola mundo", 77]

titulo = "Máster en Python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, bool))
print(comprobarTipado(verdadero, bool))