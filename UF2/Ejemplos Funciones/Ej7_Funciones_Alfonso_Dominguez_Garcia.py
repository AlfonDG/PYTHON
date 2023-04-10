caracterU = input("Introduzca un valor: ")

def aMajuscula(caracter):

    if len(caracter) == 1:

        if caracter.isalpha():

            return caracter.upper()

        else:
            return caracter
    return -1


resultado = aMajuscula(caracterU)

print(resultado)
