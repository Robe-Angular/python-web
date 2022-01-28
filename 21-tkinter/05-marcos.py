from tkinter import *
ventana = Tk()
ventana.title("Marcos | Máster en Python")
ventana.geometry("700x400")
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="#ee33ff",
    bd=5,
    relief="solid"
)
marco_padre.pack(side="bottom", fill="x", expand="yes")

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=12,
    relief="raised"
)
marco.pack(side="right", anchor=SE)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Soy un texto dentro de un marco")
texto.config(
    bg="#333eef",
    fg="#ccc",
    font=("Arial", 20),
    anchor="center",
    bd=3,
    relief=SOLID

)
texto.pack(side=LEFT, anchor="center", fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief="solid"
)
marco.pack(side="left", anchor=SW)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="solid"
)
marco_padre.pack(side="top", fill="x", expand="yes")

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="pink",
    bd=12,
    relief="raised"
)
marco.pack(side="right", anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=5,
    relief="solid"
)
marco.pack(side="left", anchor=SW)

ventana.mainloop()