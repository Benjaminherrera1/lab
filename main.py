from adjunto import D_Adjunto
from regular import D_Regular

Adjunto= D_Adjunto()
Regular= D_Regular()
Docentes_Regulares=[]
Docentes_Adjuntos=[]

def IngresarDatos():
    Nombre=input("Ingrese el nombre:").capitalize()
    Rut=input("Ingrese el Rut:").capitalize()
    td=input("Ingrese docente Adjunto o Regular:").capitalize()
    while td !="Adjunto" and "Regular":
        print("Docente mal ingresado")
        td=input("Ingrese docente Adjunto o Regular:").capitalize()

    if td=="Adjunto":
        Adjunto.SetNombreCompleto(Nombre)
        Adjunto.SetRut(Rut)
        Adjunto.SetTipoDocente(td)
        Adjunto.GetGradoAcademico(input("Ingrese el grado academico"))
        Adjunto.SetFechaContrato(input("Ingrese fecha de contrato"))
        Adjunto.SetHorasTrabajadas(int(input("Ingrese las horas trabajadas")))
        Docentes_Adjuntos.append(Adjunto)
    
    if td=="Regular":
        Regular.SetNombreCompleto(Nombre)
        Regular.SetRut(Rut)
        Regular.SetTipoDocente(td)
        Regular.GetGradoAcademico(input("Ingrese el grado academico"))
        Regular.SetFechaContrato(input("Ingrese fecha de contrato"))
        Regular.SetTipoJornada(input("Ingrese el tipo de jornada"))
        Regular.SetSueldoBase(int(input("Ingrese las horas trabajadas")))
        Docentes_Regulares.append(Regular)

def VerDatos(lista):
    for i in range(len(lista)):
        print(lista[i])

def ValidarRut():
    pass

def Main():
    op=0
    while op==0:
        IngresarDatos()
        op=int(input("Para continuar presione 0"))
    VerDatos

Main()


        

