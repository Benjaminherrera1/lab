from persona import Persona

class Docente(Persona):
    def __init__(self, nc="", r="", go="",td="", fc=""):
        super().__init__(nc, r)
        self.__Grado_Academico=go
        self.__Tipo_Docente=td
        self.__Fecha_Contrato=fc
    
    def SetGradoAcademico(self, grado):
        self.__Grado_Academico=grado
    
    def SetTipoDocente(self, td):
        self.__Tipo_Docente=td

    def SetFechaContrato(self, fc):
        self.__Fecha_Contrato=fc
    
    def GetGradoAcademico(self):
        return self.__Grado_Academico
        
    def GetTipoDocente(self):
        return self.__Tipo_Docente
        
    def GetFechaContrato(self):
        return self.__Fecha_Contrato
        
   



