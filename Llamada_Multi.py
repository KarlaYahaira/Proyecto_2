import tkinter as tk
import Principal
import Funciones

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__()

        # Creacion de los tres paneles
        login = Principal.Login(master, titulo="Contraseña para ingresar al sistema de tablas de multiplicar", ancho=360, alto=180)
        principal = Funciones.VentanaPrincipal(master, titulo="Sistema de tablas de multiplicar", ancho=600, alto=400)
        tabla = Funciones.VentanaTabla(master, titulo="Tablas multiplicar", ancho=360, alto=180)

        # Conexión entre sí de la secuencia
        login.siguiente = principal.mostrar
        principal.siguiente = tabla.mostrar
        tabla.siguiente = principal.mostrar

        # Configuración de los tres frames
        for frame in (login, principal, tabla):
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Empezamos por el de login
        login.mostrar()

def menu():

    root = tk.Tk()
    app = App(root)
    app.mainloop()

if __name__ == "__main__":
     menu()