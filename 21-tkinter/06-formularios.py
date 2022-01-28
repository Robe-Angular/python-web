from tkinter import * 

ventana = Tk()
ventana.geometry("450x400")
ventana.title("Formularios")
#Encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Víctor Robles")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
#encabezado.pack(side=LEFT, anchor="nw", fill="x", expand="yes")
encabezado.grid(row=0, column=0, columnspan=12)

#Label para el campo(Nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=E)

#campo de texto
campo_texto = Entry(ventana)
campo_texto.config(justify=RIGHT, state=NORMAL)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky="w")


#Label para el campo(Apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=E)

#campo de texto
campo_texto = Entry(ventana)
campo_texto.config(justify=LEFT, state=DISABLED)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#Label para el campo(Descripción)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=NE)

#Campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, padx=5, pady=5, sticky="w")
campo_grande.config(width=30, height=5, font=('Arial', 12), padx=15, pady=15)

#Botón
boton = Button(ventana, text="Enviar")
boton.grid(row=4, column=1, padx=5, pady=5, sticky="nw")
boton.config( bg="green", fg="white")

ventana.mainloop()