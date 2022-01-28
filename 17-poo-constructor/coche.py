#poo

#Definir una clase de ese tipo
#(Coche) con características similares
class Coche:

    #Atributos o propiedades(Variables)
    #Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soy_publico = "Hola, soy un atributo público"
    __soy_privado = "Hola soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballaje = caballaje
        self.plazas = plazas


    #Métodos, son acciones que hace le objeto(coche) -> (funciones)
    def getPrivado(self):
        return self.__soy_privado

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = "----Información del Coche----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info

#Fin definición clase

#Crear objetos / instanciar la clase
"""
#coche = Coche()

print(coche.marca, coche.color)

print(f"Velocidad actual: {coche.getVelocidad()}")
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Velocidad actual: {coche.getVelocidad()}")
coche.frenar()
coche.frenar()
print(f"Velocidad actual: {coche.getVelocidad()}")
coche.setColor('Amarillo')
coche.setModelo('Murciélago')
print("---Coche1---")
print(coche.getModelo(), coche.getColor(), coche.getVelocidad())
print("---*************---")
print("---Coche2---")
#Crear más objetos
coche2 = Coche()
coche2.setColor('Verde')
coche2.setModelo('Gallardo')
print(coche2.getModelo(), coche2.getColor(), coche2.getVelocidad())
print("---*************---")

print(type(coche2))
"""