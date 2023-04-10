__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

#Escribimos en esta variable el número de veces que desea repetir el código de las funciones.
numVeces = int(input("Introduzca N veces que desea repetir el código: "))

def crear_funcio_calculadora(n):

    #En la función de suma realizaremos el cálculo de n + num1 que será el valor de N sumado a num1. Por ejemplo:
    #Si el valor es n = 75. Entonces hará 75 + 10 = 85.
    def suma(num1):

        return n + num1

    #Ahora en la función de resta procedemos a hacer lo mismo con el valor de N restar el num2 que podría ser equivalente a n = 75 - 10 = 65.
    def resta(num2):

        return n - num2

    #En este momento debemos de devolver los valores del cáluco de suma y resta para después poder mostrarlo más adelante en el bucle While.
    return suma,resta

#Aquí escribimos el bucle WHILE loop que permitirá repetir las funciones "crear_funcio_claculadora" y sus subfunciones.
while numVeces > 0:

    #Aquí le pedimos al usuario que introduzca el valor de N a continuación.
    n = int(input("\nIntroduzca el valor de N a continuación: "))

    #Aquí estabelcemos que la suma y la resta sea igual a "crear_funcio_cal" de tal forma que devolverá el resultado del print más adelante.
    suma, resta = crear_funcio_calculadora(n)

    #Pediremos los valores num1 para la suma y num2 para el valor de la resta.
    num1 = int(input("Introduzca el valor para la suma: "))

    num2 = int(input("Introduzca el valor para la resta: "))

    #Printamos los valores de la suma y la resta.
    print("\nEl valor de la suma será -> ",suma(num1))

    print("El valor de la resta será -> ",resta(num2))

    #Aquí restaremos el contador de numVeces hasta llegar a 0.
    numVeces -= 1

print("")
print(__author__)
print(__copyright__)