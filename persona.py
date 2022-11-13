class Persona():
    def __init__(self, nc="", r=""):
        self.__Nombre_Completo=nc
        self.__Rut=r
    
    def SetNombreCompleto(self, nc):
        self.__Nombre_Completo=nc
    
    def SetRut(self, r ):
        self.__Rut=r
    
    def GetNombreCompleto(self):
        return self.__Nombre_Completo
    
    def GetRut(self):
        return self.__Rut



    

        