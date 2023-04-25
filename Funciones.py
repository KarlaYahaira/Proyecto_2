import sys
import tkinter as tk
from Principal import Panel

class VentanaPrincipal(Panel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(self, text="Resultado:").place(x=20, y=30)
        button1 = tk.Button(self, text="Tablas de Multiplicar", command=self.mostrar_tabla)
        button1.place(x=100, y=20)
        self.cajadetexto = tk.Text(self, bg="white", fg="black", insertbackground="green", height=15, width=20, insertofftime=300)
        self.cajadetexto.place(x=10, y=100)
        sys.stdout.write = self.redirector
    def redirector(self, inputStr):
        self.cajadetexto.insert(tk.INSERT, inputStr)
        return 0

    def mostrar_tabla(self):
        # Limpiar antes
        self.cajadetexto.delete("1.0", tk.END)
        self.siguiente()
class VentanaTabla(Panel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(self, text="Introduce un numero del 1 al 10" "\n" 
                            "El numero tiene que ser positivo.",).pack()
        self.numero = tk.IntVar()
        self.e1 = tk.Entry(self, textvariable=self.numero)
        self.e1.pack()
        self.update()
        tk.Button(self, text="Click", command=self.tablaMulti).pack()
    def tablaMulti(self):
        try:
            numeroInt = int(self.numero.get())
        except:
            numeroInt = -1
        if numeroInt >= 0:
            salida = []
            for i in range(0, 11):
                salida.append("{} por {} es = {}".format(numeroInt, i, numeroInt * i))
            print("\n".join(salida))
        else:
            print("El número introducido no es correcto")
        self.siguiente()
