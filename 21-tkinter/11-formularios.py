from tkinter import *


ventana = Tk()
ventana.geometry("800x300")
encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0 , columnspan=6)
#Botones Check
def mostrarProfesion():
    texto = ""
    if web.get() and movil.get():
        texto += "Desarrollo web y Desarrollo móvil"
    elif web.get():
        texto += "Desarrollo web"

    

    elif movil.get():
        texto += "Desarrollo Móvil"   

    else:
        mostrar.config(
        text=""
    )  

    if movil.get() or web.get():
        mostrar.config(
        bg="green",
        fg="#ffefee",
        text=texto
        )  
    else:
        mostrar.config(
        bg="#ccc"
    )  
       


web = IntVar()
movil = IntVar()
Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo Móvil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=1)

mostrar = Label(ventana, text="", bg="#ccc")
mostrar.grid(row=3, column=0, columnspan=2)


#Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana,text="¿Cuál es tu género?")

Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=5, column=0)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=5, column=1)

marcado= Label(ventana)
marcado.grid(row=6)

#Option
def seleccionar():
    seleccionado.config(text=opcion.get())
Label(ventana,text="Selecciona una opción").grid(row=6, column=0)
opcion = StringVar()
opcion.set("Opcion 4")
select = OptionMenu(ventana, opcion, "Opción 1", "Opción 2", "Opción 3" )
select.grid(row=7, column=0)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=7, column=2)

ventana.mainloop()