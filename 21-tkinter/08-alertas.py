from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    #Messagebox.showinfo("Info: Alerta", "Hola soy Víctor Robles")
    #Messagebox.showwarning("Warning: Alerta", "Hola soy Víctor Robles")
    #Messagebox.showerror("Error: Alerta", "Hola soy Víctor Robles")
    return True

def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")

    if resultado != "yes":
        Messagebox.showinfo("Chao",f"Adiós {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar alerta!!", command=sacarAlerta).pack()
Button(ventana, text="Salir", command= lambda: salir("VíctorRobles")).pack()


ventana.mainloop()
