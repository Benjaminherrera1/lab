from docente import Docente

class D_Regular(Docente):
    def __init__(self, nc="", rut="", grado="", td="", fc="", tj="", bs=""):
        super().__init__(nc, rut, grado, td, fc)
        self.__Tipo_Jornada=tj
        self.__Sueldo_Base=bs
    
    def SetTipoJornada(self, tj):
        self.__Tipo_Jornada=tj
    
    def SetSueldoBase(self, bs):
        self.__Sueldo_Base=bs

    def GetTipoJornada(self):
        return self.__Tipo_Jornada
    
    def GetSueldoBase(self):
        return self.__Sueldo_Base
    

    
    
    



    