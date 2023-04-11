__author__ = "Alfonso Domínguez García"
__copyright__="Copyright © 2023 Alfonso Domínguez García"


num1 = int(input("Introducir el primer valor de num1: "))

num2 = int(input("Introduzca el segundo valor de num2: "))

def multiplicacion(num1,num2):

    if num1 == 0 or num2 == 0:

        return 0

    elif num1 == 1:

        return num2

    elif num2 == 1:

        return num1

    else:
        return num1 + multiplicacion(num1,num2 - 1)

print(multiplicacion(num1,num2))


print("")

print(__author__)
print(__copyright__)