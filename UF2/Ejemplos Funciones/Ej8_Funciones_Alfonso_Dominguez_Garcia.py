import math

def calculs():

    menuSeguir = True

    while menuSeguir == True:

        print("======================")
        print("Presiona S para SUMAR")
        print("Presiona R para RAÍZ CUADRADA")
        print("Presiona L para LOGARITME")
        print("Presiona A para AYUDA")
        print("Presiona T para TERMINAR")

        seleccionOpcion = str(input("Introduzca el valor en letra de lo que deseé: ")).upper()

        if seleccionOpcion == "S":

            suma()

        elif seleccionOpcion == "R":

            arrelQuadrada()

        elif seleccionOpcion == "L":
            logaritme()

        elif seleccionOpcion == "A":
            ajuda()

        elif seleccionOpcion == "T":

            terminar()

        else:
            menuSeguir = False
            return "No ha escogido una opción válida, acabamos el programa."

def suma():
    valor1 = int(input("Introduzca un valor: "))

    valor2 = int(input("Introduzca el segundo valor: "))

    operacionSuma = valor1 + valor2

    print(operacionSuma)

def arrelQuadrada():

    valor1 = int(input("Introduzca un valor: "))

    print(math.sqrt(valor1))

def logaritme():

    valor1 = int(input("Introduzca un valor: "))

    print(math.log(valor1))

def ajuda():

    print("Esta es una función de ayuda. Ha de pulsar cualquiera de las letras siguientes en el menú -> S = Sumar | R -> Raíz Cuadrada | L -> Realizar el logaritmo de un valor | A -> Mostrar la ayuda y finalmente la T -> Para finalizar el programa.")

def terminar():

    menuSeguir = False

    print(menuSeguir)

print(calculs())

