def sum4(preu,descompte):

    if descompte >= 1 and descompte <= 100:
        return preu-preu*descompte/100

    elif descompte >= 0 and descompte < 1:
        return preu-preu*descompte

    else:
        return "Error número no válido"

preu = float(input("Precio: "))

descompte = float(input("Porcentaje de descuento: "))

resultado = sum4(preu,descompte)

print("Precio de Descuento: ",resultado)