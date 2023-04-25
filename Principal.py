from tkinter import messagebox
import tkinter as tk

class Panel(tk.Frame):

    def __init__(self, master, titulo="Sin título", ancho=500, alto=180):
        super().__init__(master)
        self.master: tk.Tk = master
        self.siguiente = (lambda: None)  # Valor por defecto no útil. El programa principal debe asignar otro
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.x = (self.master.winfo_screenwidth() - self.ancho) // 2
        self.y = (self.master.winfo_screenheight() - self.alto) // 2

    def mostrar(self):
        self.master.title(self.titulo)
        self.master.geometry("{}x{}+{}+{}".format(self.ancho, self.alto, self.x, self.y))
        self.lift()

class Login(Panel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        tk.Label(self, text="Introduce tu usuario y contraseña para entrar al mundo de la multiplicación", fg="black",).place(x=20, y=10)
        tk.Label(self, text="Username :", fg="black").place(x=70, y=60)
        tk.Label(self, text="Password :", fg="black").place(x=70, y=90)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Entry(self, textvariable=self.username).place(x=150, y=60)
        tk.Entry(self, textvariable=self.password, show="*").place(x=150, y=90)
        tk.Button(self, text="Iniciar", command=self.login).place(x=150, y=120)

    def login(self):
        if self.username.get() != "karla" and self.password.get() != "karla":
            messagebox.showinfo(title="Inicio de sesión", message="Bienvenido al mundo de la multiplicación")
            self.siguiente()
        else:
            messagebox.showerror(title="Error de inicio", message="Usuario/Contraseña Incorrectos")

