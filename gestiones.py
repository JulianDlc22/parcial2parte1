from clases import Candidata, Jurado, Calificacion

class GestionesCandidata:

    def __init__(self):
        self.candidata = {}

    def cargar_candidata(self):

        try:
            with open("candidatas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo_candidata, nombre, edad, institucion_educativa, municipio = linea.split(
                            ":")
                        self.candidata[codigo_candidata] = Candidata(codigo_candidata, nombre, edad, institucion_educativa, municipio)

                print("Candidatas importados desde candidatas.txt")

        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará uno nuevo al guardar.")

    def guardar_candidata(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for codigo_candidata, datos in self.candidata.items():
                archivo.write(
                    f"{codigo_candidata}:{datos.nombre}:{datos.edad}:{datos.institucion_educativa}:{datos.municipio}\n")





class GestionesJurado:
    def __init__(self,):
        self.jurado = {}

    def cargar_jurado(self):

        try:
            with open("jurado.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo_jurado, nombre, especialidad, calificacion = linea.split(
                            ":")
                        self.jurado[codigo_jurado] = Jurado(codigo_jurado, nombre, especialidad,calificacion)

                print("Jurados importados desde jurados.txt")

        except FileNotFoundError:
            print("No existe el archivo jurado.txt, se creará uno nuevo al guardar.")

    def guardar_jurados(self):
        with open("jurado.txt", "w", encoding="utf-8") as archivo:
            for codigo_jurado, datos in self.jurado.items():
                archivo.write(
                    f"{codigo_jurado}:{datos.nombre}:{datos.especialida}:{datos.calificacion}\n")

class GestionesCalificacion:
    def __init__(self,):
        self.calificacion = {}

    def cargar_calificacion(self):

        try:
            with open("calificaciones.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cod_calificaion, codigo_jurado, codigo_candidata, cultura_general, proyeccion_escenica, entrevista = linea.split(
                            ":")
                        self.calificacion[codigo_jurado] = Calificacion(cod_calificaion, codigo_jurado, codigo_candidata,cultura_general, proyeccion_escenica, entrevista)

                print("Calificaciones importados desde calificaciones.txt")

        except FileNotFoundError:
            print("No existe el archivo calificaciones.txt, se creará uno nuevo al guardar.")

    def guardar_jurados(self):
        with open("calificaciones.txt", "w", encoding="utf-8") as archivo:
            for cod_calificacion, datos in self.calificacion.items():
                archivo.write(
                    f"{cod_calificacion}:{datos.codigo_jurado}:{datos.codigo_candidata}:{datos.cultura_general}:{datos.proyeccion_escenica}:{datos.entrevista}\n")



