#Condicional if

##################Ejemplo 1#######################
print("###Ejemplo1###")
#color = input('Adivina cuál es mi color favorito: ')
color = 'rojo'
if color == 'rojo':
    print('El color es Rojo')
else:
    print('Color incorrecto')

##################Ejemplo 2#######################
print("###Ejemplo2###")

year = 2020
#year = int(input('¿En qué año estamos?: '))

if year >= 2021:
    print('Estamos en 2021 en adelante')
else:
    print('Es un año anterior a 2021')

##################Ejemplo 3#######################
print("###Ejemplo3###")

nombre = "Victor Robles"
ciudad = "Cuernavaca"
continente = "América"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f'{nombre} es mayor de edad')
    
    if continente != "Europa":
        print(f"{nombre} no es europeo")
    else:
        print(f"{nombre} es europeo y de {ciudad}")
else:
    print(f'{nombre} no es mayor de edad')

##################Ejemplo 4#######################
print("###Ejemplo4###")

#dia = int(input('Dia: '))
dia = 1
"""
if dia == 1:
    print('Es lunes')
else:
    if dia == 2:
        print('Es martes')
    else:
        if dia == 3:
            print('Es miércoles')
        else:
            if dia == 3:
                print('Es miércoles')
            else:
                if dia == 4:
                    print('Es jueves')
                else:
                    if dia == 5:
                        print('Es viernes')
                    else:
                        if dia == 6:
                            print('Es sábado')
                        else:
                            if dia == 7:
                                print('Es domingo')
                            else:
                                print('No existe ese día')
"""
if dia == 1:
    print('Es lunes')
elif dia == 2:
    print('Es martes')
elif dia == 3:
    print('Es miércoles')
elif dia == 4:
    print('Es jueves')
elif dia == 5:
    print('Es viernes')
elif dia == 6:
    print('Es sábado')
elif dia == 7:
    print('Es domingo')
else:
    print('El día no existe')

##################Ejemplo 5#######################
print("###Ejemplo5###")

edad_minima = 18
edad_maxima = 65
##edad_oficial = int(input('Edad: '))
edad_oficial = 23

if edad_oficial >= 18 and edad_oficial <= 65:
    print('Está en edad de trabajar')
else:
    print('No está en edad de trabajar')

##################Ejemplo 5#######################
"""
print("###Ejemplo5###")
pais = "Alemania"
pais = input("País: ")
if  pais == 'México' or pais == 'España' or pais == 'Colombia':
    print(F"{pais} es un país de habla hispana")
else:
    print(F"{pais} no es un país de habla hispana")
"""
##################Ejemplo 6#######################
"""
print("###Ejemplo6###")
#pais = "Alemania"
pais = input("País: ")
if  not(pais == 'México' or pais == 'España' or pais == 'Colombia'):
    print(F"{pais} no es un país de habla hispana")
else:
    print(F"{pais} es un país de habla hispana")
"""
##################Ejemplo 6#######################
print("###Ejemplo6###")
#pais = "Alemania"
pais = input("País: ")
if  pais != 'México' and pais != 'España' and pais != 'Colombia':
    print(F"{pais} no es un país de habla hispana")
else:
    print(F"{pais} es un país de habla hispana")