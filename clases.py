class Candidata:
    def __init__(self, codigo_candidata, nombre, edad, institucion_educativa, municipio):
        self.codigo_candidata = codigo_candidata
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion_educativa
        self.municipio = municipio

class Jurado:
    def __init__(self,codigo_jurado,  nombre, especialidad, calificacion):
        self.codigo_jurado = codigo_jurado
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificacion = calificacion

class Calificacion:
    def __init__(self, cod_calificacion,codigo_jurado, codigo_candidata, cultura_general, proyeccion_escenica, entrevista):
        self.cod_calificacion = cod_calificacion
        self.codigo_jurado = codigo_jurado
        self.codigo_candidata = codigo_candidata
        self.cultura_general = cultura_general
        self.proyeccion_escenica = proyeccion_escenica
        self.entrevista = entrevista



