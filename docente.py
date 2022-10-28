from persona import Persona

class Docente(Persona):
    def __init__(self, nc="", rut="", grado="",td="", fc=""):
        super().__init__(nc, rut)
        self.__Grado_academico=grado
        self.__Tipo_docente=td
        self.__Fecha_contrato=fc

def get_Grado_academico(self):
    return self.__Grado_academico

def set_Grado_academico(self, grado):
    self.__Grado_academico=grado

def get_Tipo_docente(self):
    return self.__Tipo_docente

def set_Tipo_docente(self, td):
    self.__Tipo_docente=td

def get_Fecha_contrato(self):
    return self.__Fecha_contrato

def set_Fecha_contrato(self, fc):
    self.__Fecha_contrato=fc



