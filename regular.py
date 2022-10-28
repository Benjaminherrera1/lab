from docente import Docente

class D_Regular(Docente):
    def __init__(self, nc="", rut="", grado="", td="", fc="", tj=""):
        super().__init__(nc, rut, grado, td, fc)
        self.__Tipo_jornada=tj

def get_Tipo_jornada(self):
    return self.__Tipo_jornada

def set_tipo_jornada(self, tj):
    self.__Tipo_jornada=tj



    