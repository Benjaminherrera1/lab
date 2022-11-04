peso_disco = float(input("Ingrese el peso deseado: "))
peso = [0.3575, 0.3075, 0.1575, 0.1775]
peso_final = [i * peso_disco for i in peso]
print("Arena: " + str(round(peso_final[0], 4)) + str(" Kg"))
print("Cemento: " + str(round(peso_final[1], 4)) + str(" Kg"))
print("Agua: " + str(round(peso_final[2], 4)) + str(" Kg"))
print("Piedra: " + str(round(peso_final[3], 5)) + str(" Kg"))



