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
    #Métodos, son acciones que hace le objeto(coche) -> (funciones)
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

#Fin definición clase

#Crear objetos / instanciar la clase
coche = Coche()

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