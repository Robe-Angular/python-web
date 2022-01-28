from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola soy Víctor").pack(anchor=E)

imagen = Image.open("./imagenes/lobo.jpg")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor="w")

ventana.mainloop()
