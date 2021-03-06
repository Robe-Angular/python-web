#Tkinter es un módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Máster en python con Víctor Robles"
        self.icon = "./imagenes/logotipo.ico"
        self.icon_alt = "./21-tkinter/imagenes/logotipo.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        #Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.title)

        #Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        """
        ruta_icono = "C:/wamp64/www/master-python/21-tkinter/imagenes/logotipo.ico"
        """
        #Mostrar texto en el programa
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        #Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        #Cambio en el tamaño en la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)        

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#Instanciar mi programaa

programa = Programa()
programa.cargar()
programa.addTexto('Hola')
programa.addTexto('Soy un texto')
programa.addTexto('Hola amigos')
programa.addTexto('Soy un texto')
programa.mostrar()
