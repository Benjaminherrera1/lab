from docente import Docente

class D_Adjunto(Docente):
    def __init__(self, nc="", rut="", grado="", td="", fc="", ht=0):
        super().__init__(nc, rut, grado, td, fc)
        self.__Horas_trabajadas=ht

def get_Horas_trabajadas(self):
    return self.__Horas_trabajadas

def set_Horas_trabajadas(self, ht):
    self.__Horas_trabajadas=ht


