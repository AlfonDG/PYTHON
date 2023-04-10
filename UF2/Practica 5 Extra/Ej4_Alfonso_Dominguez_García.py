__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

numVeces = int(input("Introduzca N veces que desea repetir el código: "))

def crear_funcio_calculadora(n):

    def suma(num1):

        return n + num1

    def resta(num2):

        return n - num2

    return suma, resta

while numVeces > 0:

    n = int(input("Introduzca el valor de N a continuación: "))

    suma, resta = crear_funcio_calculadora(n)

    num1 = int(input("Introduzca el valor para la suma: "))

    num2 = int(input("Introduzca el valor para la resta: "))

    print(suma(num1))

    print(resta(num2))

    numVeces -= 1

print("")
print(__author__)
print(__copyright__)