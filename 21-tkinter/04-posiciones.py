from tkinter import *

ventana = Tk()
#ventana.geometry("800x500")

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#EF3251",
    padx=50,
    pady=20,
    font=("Consolas", 30)
    )
texto.pack()

texto = Label(ventana, text="Soy Víctor Robles")
texto.config(    
    height=3,
    font=("Arial, 18"),
    padx=10,
    pady=20,
    bg="orange",
    cursor="spider"
)
texto.pack(side=TOP, fill="x", expand="yes")

texto = Label(ventana, text=('TB'))
texto.config(    
    padx=10,
    pady=20,
    bg="orange",
    cursor="spider",
    font=("Consolas", 30)
)
texto.pack(side="left", fill="x", expand="yes")

texto = Label(ventana, text="TB")
texto.config(
    fg="orange",
    bg="#EF3251",
    padx=10,
    pady=20,
    font=("Consolas", 30)
    )
texto.pack(side="left", fill="x", expand="yes")

texto = Label(ventana, text="TB")
texto.config(
    fg="red",
    bg="green",
    padx=10,
    pady=20,
    font=("Consolas", 30)
    )
texto.pack(side="left", fill="x", expand="yes")

ventana.mainloop()

