#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Víctor Robles Web"))
#print(mimodulo.calculadora(3, 5, True))
print(holaMundo("Víctor Robles Web"))
print(calculadora(3, 5, True))

#Módulo fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/Y, %H:%M:%S")
print(f"Mifecha personalizada: {fecha_personalizada}")
print(datetime.datetime.now().timestamp())

#Módulo math
import math
print(f"Raíz cuadrada de 10: {math.sqrt(10)}")
print(f"Número pi: {math.pi}")
print(f"Redondear: {math.ceil(math.pi)}")
print(f"Redondear: {math.floor(math.pi)}")

import random
print(f"Número aleatorio entre 15 y 67: {random.randint(15,67)}")
