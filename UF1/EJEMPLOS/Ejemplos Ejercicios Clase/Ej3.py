#Puedes poner la opción de Grados en tipo FLOAT input de tal forma que pueda escribir decimales

temp = float(input("Escriba la temperatura en ºC Centigrados: "))

print("MNEÚ GRADOS")
print("******************")
print("ºK | 273.15 + ºC")
print("ºF | (9/5)ºC + 32")
print("ºRankie | (9/5)(ºC+273.15)" )
print("ºRéaumur | (4/5)ºC")
print("*******************")

grado = input("Escriba el nombre del medidor, Kelvin, Fharenheit, Rankie o Réaumur: ")

if grado == "K":
    resultadoKelvin = temp + 273.15

    print("La temperatura será de ", resultadoKelvin, "ºK")

elif grado == "F":
    resultadoF = (9/5)*temp+32

    print("La temperatura será de ", resultadoF, "ºF")


elif grado == "Rankie":
    resultadoRankie = (9/5)*(temp + 273.15)

    print("La temperatura será de ", resultadoRankie, "ºRankie")

elif grado == "Réaumur":
    resultadoReaumur = (4/5)*temp

    print("La temperatura será de ", resultadoReaumur, "ºRéaumur")