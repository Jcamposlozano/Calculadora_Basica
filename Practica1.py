from tkinter import *
from Calculadora import *

class Practica1:
    
    def __init__(self):
        self.root = Tk()
        self.calculadora = Calculadora()
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.resultado = StringVar()
        self.formulario()
        

    def sumar(self):
        self.resultado.set(self.calculadora.operacion(float(self.n1.get()),float(self.n2.get()),"SUMA"))
        self.borrar()

    def resta(self):
        self.resultado.set(self.calculadora.operacion(float(self.n1.get()),float(self.n2.get()),"RESTA"))
        self.borrar()

    def multiplica(self):
        self.resultado.set(self.calculadora.operacion(float(self.n1.get()),float(self.n2.get()),"MULTIPLICA"))
        self.borrar()

    def divide(self):
        self.resultado.set(self.calculadora.operacion(float(self.n1.get()),float(self.n2.get()),"DIVIDE"))
        self.borrar()        


    def borrar(self):
        self.n1.set("")
        self.n2.set("")

    def formulario(self):
        # Configuración de la raíz
        self.root.config(bd=15)

        Label(self.root, text="Número 1").pack()
        Entry(self.root, justify="center", textvariable=self.n1).pack()

        Label(self.root, text="Número 2").pack()
        Entry(self.root, justify="center", textvariable=self.n2).pack()

        Label(self.root, text="Resultado").pack()
        Entry(self.root, justify="center", textvariable=self.resultado, state="disabled").pack()

        Label(self.root, text="").pack()  # Separador

        Button(self.root, text="+", command=self.sumar).pack(side="left")
        Button(self.root, text="-", command=self.resta).pack(side="left")
        Button(self.root, text="*", command=self.multiplica).pack(side="left")
        Button(self.root, text="/", command=self.divide).pack(side="left")

        # Finalmente bucle de la aplicación
        self.root.mainloop()