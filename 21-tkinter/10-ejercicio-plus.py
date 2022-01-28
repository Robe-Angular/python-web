#Calculadora
from tkinter import *
from tkinter import messagebox

class Calculadora:
    

    def __init__(self) -> None:
        self.ventana = Tk()
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        pass

    def sumar(self):
        try:
            operacion = float(self.numero1.get()) + float(self.numero2.get())
            self.resultado.set(operacion)
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def restar(self):
        try:
            operacion = float(self.numero1.get()) - float(self.numero2.get())
            self.resultado.set(operacion)
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def multiplicar(self):
        try:
            operacion = float(self.numero1.get()) * float(self.numero2.get())
            self.resultado.set(operacion)
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def dividir(self):
        try:
            operacion = float(self.numero1.get()) / float(self.numero2.get())
            self.resultado.set(operacion)
            messagebox.showinfo("Resultado",f"{self.resultado.get()}")
        
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def reset(self):
        messagebox.showinfo("Reseteando",f"El resultado es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")
        self.resultado.set("")

calculadora = Calculadora()

calculadora.ventana.title("Ejercicio completo con Tkinter")
calculadora.ventana.geometry("400x400")
calculadora.ventana.config(bd=25)





marco=Frame(calculadora.ventana, width=250, height=250)
marco.config(
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor="center")
marco.pack_propagate(False)

Label(marco, text="Primer número").pack()
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack()

Label(marco, text="Segundo número").pack()
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack()

Label(marco, textvariable=calculadora.resultado).pack()
Label(marco, text="")

Button(marco, text="Sumar", command=calculadora.sumar).pack(side=LEFT)
Button(marco, text="Restar", command=calculadora.restar).pack(side=LEFT)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side=LEFT)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side=LEFT)


marco=Frame(calculadora.ventana, width=250, height=250)
marco.pack(side=TOP, anchor="center")
marco.pack_propagate(False)

Button(marco, text="Resetear", command=calculadora.reset).pack(side=TOP)
calculadora.ventana.mainloop()

