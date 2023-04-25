import tkinter
from tkinter import *
import random

class sumasrapidas():
    def __init__(self, vidas):
        root = Tk()
        self.num1 = IntVar()
        self.vidas = vidas
        self.rango_numero1 = random.randint(0, 50)
        self.rango_numero2 = random.randint(0, 50)
        self.root = root
        self.root.configure(background="orange")
        self.root.title("Juego piensa rápido el resultado de sumar")
        self.root.maxsize("500", "500")
        self.root.minsize("300", "200")
        Label(self.root, text="Piensa Rápido", bg="white", fg="green").grid(row=5, column=8)
        self.captura = Entry(self.root, textvariable=self.num1)
        self.aceptar = Button(self.root, text="Aceptar", command=self.suma, fg="green", bg="white")
        self.captura.grid(row=6, column=8)
        self.aceptar.grid(row=7, column=8)
        Label(self.root, text=str(self.rango_numero1) + "+" + str(self.rango_numero2), bg="white", fg="green").grid(row=8, column=8)

    def suma(self):
        if int(self.captura.get()) == self.rango_numero1 + self.rango_numero2:
            Label(self.root, text="Correcto", bg="white", fg="green").grid(row=9, column=8)
            Label(self.root, text="Tienes " + str(self.vidas) + " vidas", bg="white", fg="green").grid(row=10, column=8)
        else:
            Label(self.root, text="Incorrecto", bg="white", fg="green").grid(row=9, column=8)
            self.vidas -= 1
            Label(self.root, text="Tienes " + str(self.vidas) + " vidas", bg="white", fg="green").grid(row=10, column=8)
        if self.vidas == 0:
            Label(self.root, text="Juego Terminado", bg="white", fg="green").grid(row=11, column=8)
            exit(0)

        self.rango_numero1 = random.randint(0, 50)
        self.rango_numero2 = random.randint(0, 50)
        Label(self.root, text=str(self.rango_numero1) + "+" + str(self.rango_numero2), bg="white", fg="green").grid(row=8, column=8)

if __name__ == "__main__":
    root = Tk()
    vidas = 3
    instancia = sumasrapidas(root, vidas)
    root.mainloop()