num1 = int(input("Introduzca el valor de num1: "))

num2 = int(input("Introduzca el valor de num2: "))


def sumar(num1,num2):

    print("")

    return "El resultado de la suma es -> ", num1 + num2

def restar(num1,num2):

    print("")

    return "El resultado de la resta es -> ", num1 - num2

def multiplicar(num1,num2):

    print("")

    return "El resultado de la multiplicación es -> ", num1 * num2

def dividir(num1,num2):

    print("")

    try:
        return "El resultado de la división es -> ",num1 / num2

    except ZeroDivisionError:

        return "!!!Está intentando dividir entre 0. Vuelva a intentarlo!!!"

print(sumar(num1,num2))

print(restar(num1,num2))

print(multiplicar(num1,num2))

print(dividir(num1,num2))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)