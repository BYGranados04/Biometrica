import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Huellas")
        self.root.geometry("400x530")
        self.root.configure(bg="#b2d8d8")
        self.root.resizable(False, False)
        self.ventana_login()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ventana_login(self):
        self.limpiar_pantalla()

        # Ícono de usuario
        canvas = tk.Canvas(self.root, width=80, height=80, bg="#b2d8d8", highlightthickness=0)
        canvas.place(relx=0.5, y=80, anchor=tk.CENTER)
        canvas.create_oval(5, 5, 75, 75, fill="#1e3d59", outline="")
        canvas.create_text(40, 40, text="👤", font=("Segoe UI", 32), fill="white")

        # Panel de login
        panel = tk.Frame(self.root, bg="#1e3d59", width=340, height=270)
        panel.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        # Email
        tk.Label(panel, text="👤  Email ID", bg="#1e3d59", fg="white", anchor="w", font=("Segoe UI", 10)).place(x=30, y=30)
        self.entry_user = ttk.Entry(panel, width=30)
        self.entry_user.place(x=30, y=55)

        # Contraseña
        tk.Label(panel, text="🔒  Password", bg="#1e3d59", fg="white", anchor="w", font=("Segoe UI", 10)).place(x=30, y=95)
        self.entry_pass = ttk.Entry(panel, width=30, show="*")
        self.entry_pass.place(x=30, y=120)

        # Botón LOGIN
        btn_login = tk.Button(panel, text="LOGIN", command=self.validar_login,
                              font=("Segoe UI", 11, "bold"), bg="#0f3057", fg="white",
                              activebackground="#084d6e", width=30, relief="flat")
        btn_login.place(x=30, y=180)

        # Botón CREAR CUENTA
        btn_registrar = tk.Button(self.root, text="Crear nueva cuenta", command=self.ventana_registro,
                                  font=("Segoe UI", 10, "underline"), bg="#b2d8d8",
                                  fg="#0f3057", bd=0, cursor="hand2")
        btn_registrar.place(relx=0.5, y=490, anchor=tk.CENTER)

    def validar_login(self):
        usuario = self.entry_user.get()
        clave = self.entry_pass.get()
        if usuario and clave:
            messagebox.showinfo("Huella", f"{usuario}, coloca tu huella para verificar acceso.")
            self.ventana_bienvenida(usuario)
        else:
            messagebox.showerror("Error", "Completa ambos campos.")

    def ventana_bienvenida(self, usuario):
        self.limpiar_pantalla()

        tk.Label(self.root, text="✅ Acceso Concedido", font=("Segoe UI", 18, "bold"), bg="#b2d8d8", fg="#0f3057").pack(pady=40)
        tk.Label(self.root, text=f"Bienvenido, {usuario}", font=("Segoe UI", 14), bg="#b2d8d8", fg="#1e3d59").pack(pady=10)

        tk.Button(self.root, text="Cerrar sesión", command=self.ventana_login,
                  font=("Segoe UI", 10), bg="#0f3057", fg="white", relief="flat", width=20).pack(pady=20)

    def ventana_registro(self):
        self.limpiar_pantalla()

        # Título
        tk.Label(self.root, text="📝 Registro de Usuario", font=("Segoe UI", 16, "bold"), bg="#b2d8d8").pack(pady=20)

        # Panel de registro
        panel = tk.Frame(self.root, bg="#1e3d59", width=340, height=360)
        panel.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # Nombre
        tk.Label(panel, text="👤  Nombre completo", bg="#1e3d59", fg="white", font=("Segoe UI", 10), anchor="w").place(x=30, y=20)
        self.entry_nombre = ttk.Entry(panel, width=30)
        self.entry_nombre.place(x=30, y=45)

        # Teléfono
        tk.Label(panel, text="📱  Teléfono", bg="#1e3d59", fg="white", font=("Segoe UI", 10), anchor="w").place(x=30, y=85)
        self.entry_telefono = ttk.Entry(panel, width=30)
        self.entry_telefono.place(x=30, y=110)
        self.entry_telefono.bind("<KeyRelease>", self.validar_telefono)

        # Contraseña
        tk.Label(panel, text="🔒  Contraseña", bg="#1e3d59", fg="white", font=("Segoe UI", 10), anchor="w").place(x=30, y=150)
        self.entry_clave = ttk.Entry(panel, width=30, show="*")
        self.entry_clave.place(x=30, y=175)

        # Botón REGISTRAR
        btn_registrar = tk.Button(panel, text="Registrar", command=self.registrar_usuario,
                                  font=("Segoe UI", 11, "bold"), bg="#0f3057", fg="white",
                                  activebackground="#084d6e", width=30, relief="flat")
        btn_registrar.place(x=30, y=230)

        # Botón VOLVER
        tk.Button(self.root, text="← Volver al Login", command=self.ventana_login,
                  font=("Segoe UI", 10), bg="#b2d8d8", fg="#0f3057", bd=0).place(relx=0.5, y=500, anchor=tk.CENTER)

    def validar_telefono(self, event):
        contenido = self.entry_telefono.get()
        if not contenido.isdigit():
            self.entry_telefono.delete(0, tk.END)
            self.entry_telefono.insert(0, ''.join(filter(str.isdigit, contenido)))
            self.root.bell()

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        clave = self.entry_clave.get()
        if nombre and telefono and clave:
            messagebox.showinfo("Huella", f"{nombre}, coloca tu huella para finalizar el registro.")
        else:
            messagebox.showerror("Error", "Completa todos los campos.")

# Iniciar app
root = tk.Tk()
app = App(root)
root.mainloop()
