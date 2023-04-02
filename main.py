import sys
import tkinter as tk
from tkinter import messagebox


class Panel(tk.Frame):
    """Clase genérica para mostrar un Frame con un cierto título y
    tamaño dados, centrado en la pantalla"""

    def __init__(self, master, titulo="Sin título", ancho=360, alto=180):
        super().__init__()
        self.master: tk.Tk = master
        self.siguiente = (
            lambda: None
        )  # Valor por defecto no útil. El programa principal debe asignar otro
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.x = (self.master.winfo_screenwidth() - self.ancho) // 2
        self.y = (self.master.winfo_screenheight() - self.alto) // 2

    def mostrar(self):
        self.master.title(self.titulo)
        self.master.geometry(
            "{}x{}+{}+{}".format(self.ancho, self.alto, self.x, self.y)
        )
        self.lift()


class Login(Panel):
    """Panel de login. Cuando el nombre y contraseña se introducen bien
    llamará a self.siguiente() para pasar al siguiente Panel"""

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(
            self,
            text="Introduce tu usuario y contraseña para entrar a tu mundo",
            fg="black",
        ).place(x=20, y=10)
        tk.Label(self, text="Username :", fg="black").place(x=20, y=60)
        tk.Label(self, text="Password :", fg="black").place(x=20, y=90)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Entry(self, textvariable=self.username).place(x=90, y=60)
        tk.Entry(self, textvariable=self.password, show="*").place(x=90, y=90)
        tk.Button(self, text="Login", command=self.login).place(x=90, y=120)

    def login(self):
        if self.username.get() == "yo" and self.password.get() == "yo":
            messagebox.showinfo(title="Login Status", message="You have logged in")
            self.siguiente()
        else:
            messagebox.showerror(title="Login Error", message="User/Password Incorrect")


class VentanaPrincipal(Panel):
    """Panel que muestra una "terminal" negra y el botón para generar la tabla.
    Al pulsar ese botón llama a self.siguiente() para mostrar el panel que
    pide un número al usuario"""

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(self, text="Tablas de Multiplicar :").place(x=320, y=300)
        button1 = tk.Button(
            self, text="Tablas de Multiplicar", command=self.mostrar_tabla
        )
        button1.place(x=400, y=20)
        self.cajadetexto = tk.Text(
            self,
            bg="black",
            fg="orange",
            insertbackground="green",
            height=25,
            width=30,
            insertofftime=400,
        )
        self.cajadetexto.place(x=10, y=20)
        sys.stdout.write = self.redirector

    def redirector(self, inputStr):
        """Esta función redirige la salida estándar a la "terminal" del panel"""
        self.cajadetexto.insert(tk.INSERT, inputStr)
        return 0

    def mostrar_tabla(self):
        # Limpiar antes
        self.cajadetexto.delete("1.0", tk.END)
        self.siguiente()


class VentanaTabla(Panel):
    """Este panel pide un número al usuario y verifica que sea correcto. Si no
    lo es imprime un mensaje de error, si lo es imprime una tabla de
    multiplicar. En ambos casos llama a self.siguiente() para pasar
    al panel siguiente, que en este caso sería el antes visto donde
    se haría visible el mensaje o tabla impresos."""

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(
            self,
            text="Introduce el Numero de la tabla de"
            "multiplar que quieres aprender.\n"
            "El numero tiene que ser positivo.",
        ).pack()
        self.numero = tk.IntVar()
        self.e1 = tk.Entry(self, textvariable=self.numero)
        self.e1.pack()
        self.update()
        tk.Button(self, text="Generar", command=self.tablaMulti).pack()

    def tablaMulti(self):
        try: # Capturamos posible excepción por si introduce algo que
             # no es un número
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


class App(tk.Frame):
    """Clase principal que crea los diferentes paneles y los "conecta" entre
    sí de modo que la función .siguiente() de uno llame al .mostrar() del
    siguiente"""

    def __init__(self, master):
        super().__init__()

        # Creacion de los tres paneles
        login = Login(master, titulo="MyLittleWorld Login", ancho=360, alto=180)
        principal = VentanaPrincipal(
            master, titulo="MyLittleWorld System", ancho=600, alto=400
        )
        tabla = VentanaTabla(master, titulo="Tabla multiplicar", ancho=360, alto=180)

        # Conexión entre sí de la secuencia
        login.siguiente = principal.mostrar
        principal.siguiente = tabla.mostrar
        tabla.siguiente = principal.mostrar

        # Configuración de los tres frames
        for frame in (login, principal, tabla):
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Empezamos por el de login
        login.mostrar()


def main():
    """El programa principal instancia la ventana raiz Tk() y la usa
    para inicializar la aplicación y el bucle de eventos"""
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()