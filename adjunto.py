from docente import Docente

class D_Adjunto(Docente):
    def __init__(self, nc="", rut="", grado="", td="", fc="", ht=""):
        super().__init__(nc, rut, grado, td, fc)
        self.__Horas_trabajadas=ht
        
    def SetHorasTrabajadas(self, ht):
        self.__Horas_trabajadas=ht

    def GetHorasTrabajadas(self):
        return self.__Horas_trabajadas
        
    


