caracterU = input("Introduzca un valor: ")

def esLletra(caracter):

    if caracter.isalpha():

        return 1

    elif caracter.isdigit():

        return 0

print(esLletra(caracterU))