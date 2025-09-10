import tkinter as tk
from tkinter import messagebox

class CertamenIndependicia2025():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Certamen Independencia 2025")
        self.ventana.geometry("500x500")
        self.menu()
        tk.Label(text="Certamen Independencia 2025", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(self.ventana, text="Cargar Datos").pack(pady=5)
        self.ventana.mainloop()


    def menu(self):
        barra =tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar Candidata", command=self.registarcandidata)
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def registarcandidata(self):
        ventana_inscribir =tk.Toplevel(self.ventana)
        ventana_inscribir.title("Registro de Candidatas")
        ventana_inscribir.geometry("300x500")
        tk.Label(ventana_inscribir, text="Codigo de Candidata:").pack(pady = 5)
        codigo_candidata = tk.Entry(ventana_inscribir).pack(pady = 5)
        tk.Label(ventana_inscribir, text="Nombre de Candidata:").pack(pady=5)
        nombre_candidata = tk.Entry(ventana_inscribir).pack(pady=5)
        tk.Label(ventana_inscribir, text="Edad de Candidata:").pack(pady=5)
        edad_candidata = tk.Entry(ventana_inscribir).pack(pady=5)
        tk.Label(ventana_inscribir, text="Insitucion Educativa:").pack(pady=5)
        institucion_educativa_candidata = tk.Entry(ventana_inscribir).pack(pady=5)
        tk.Label(ventana_inscribir, text="Municipio:").pack(pady=5)
        municipio_candidata = tk.Entry(ventana_inscribir).pack(pady=5)
        boton_inscribir = tk.Button(ventana_inscribir, text="Guardar", command=lambda:self.mensaje_exitoso("Registro Exitoso", "Candidata Registrada")).pack(pady=10)

    def mensaje_exitoso(self,titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
if __name__ == "__main__":
    CertamenIndependicia2025()