from tkinter import *
import Sumas
import Llamada_Multi
def suma2():
    suma1 = Sumas.sumasrapidas(3)
def tablas():
    tabla1 = Llamada_Multi.menu()

root = Tk()
root.title("Interactuar con los niños")
barramenu = Menu(root)
juegoeduca = Menu(barramenu, tearoff=0)
juegoeduca.add_command(label="Tablas de multiplicar", command=tablas)
juegoeduca.add_command(label="Que tal ágil es tu mente con la suma", command=suma2)
juegoeduca.add_separator()
juegoeduca.add_command(label="Salida", command=root.quit)

barramenu.add_cascade(label="Juegos educativos", menu=juegoeduca)
root.config(menu=barramenu)
root.mainloop()