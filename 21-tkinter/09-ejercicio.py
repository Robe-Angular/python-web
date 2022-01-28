#Calculadora
from tkinter import *
from tkinter import messagebox

def sumar():
    try:
        operacion = float(numero1.get()) + float(numero2.get())
        resultado.set(operacion)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

def restar():
    try:
        operacion = float(numero1.get()) - float(numero2.get())
        resultado.set(operacion)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

def multiplicar():
    try:
        operacion = float(numero1.get()) * float(numero2.get())
        resultado.set(operacion)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

def dividir():
    try:
        operacion = float(numero1.get()) / float(numero2.get())
        resultado.set(operacion)
        messagebox.showinfo("Resultado",f"{resultado.get()}")
    
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

def reset():
    messagebox.showinfo("Reseteando",f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")
    resultado.set("")


ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)



numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco=Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor="center")
marco.pack_propagate(False)

Label(marco, text="Primer número").pack()
Entry(marco, textvariable=numero1, justify=CENTER).pack()

Label(marco, text="Segundo número").pack()
Entry(marco, textvariable=numero2, justify=CENTER).pack()

Label(marco, textvariable=resultado).pack()
Label(marco, text="")

Button(marco, text="Sumar", command=sumar).pack(side=LEFT)
Button(marco, text="Restar", command=restar).pack(side=LEFT)
Button(marco, text="Multiplicar", command=multiplicar).pack(side=LEFT)
Button(marco, text="Dividir", command=dividir).pack(side=LEFT)


marco=Frame(ventana, width=250, height=250)
marco.pack(side=TOP, anchor="center")
marco.pack_propagate(False)

Button(marco, text="Resetear", command=reset).pack(side=TOP)
ventana.mainloop()

