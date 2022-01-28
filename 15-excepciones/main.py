"""
#Capturar excepciones y manejar errores en código
#Susceptible a fallos/errores
try:
    nombre = input("¿Cuál es tu nombre? ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
        
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo ha ido bien")
finally:
    print("Fin de la iteración")
#Excepciones personalizadas o lanzar excepción
"""
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input('Introduce la edad: '))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print("Bienvenido al Máster en Python")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print(f'Existe un error: {e}')