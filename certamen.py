import tkinter as tk

class CertamenIndependicia2025():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Certamen Independence 2025")
        self.ventana.geometry("500x500")
        tk.Label()
        tk.Button(self.ventana).pack(pady=5)
        self.ventana.mainloop()



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
