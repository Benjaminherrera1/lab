import math

Multi=[2, 3, 4, 5, 6, 7, 2, 3]
Rut=[9, 0, 4, 2, 6, 9, 7, 2]

Sumar_rut=sum(Multi)

Divi_rut=Sumar_rut/11
Numero_int=math.trunc(Divi_rut)
Numero_multi=Numero_int*11

Operacion=Sumar_rut-Numero_multi
Resultado=11-Operacion


'''Ejemplo'''
rt = input("Ingrese rut")
serie = 2
acc = 0
for r in range(len(rt)):
    print(rt[r],'*',str(serie))
    acc += int(rt[r]) * serie
    serie += 1
    if serie > 7:
        serie = 2
print(acc)
#print(Resultado)