num1 = int(input("Introduzca el primer valor: "))

num2 = int(input("Introduzca el segundo valor: "))

def cociente(num1,num2):

    try:

        resultado = num1 / num2

        return resultado

    except ZeroDivisionError:

        print("Error, no puede dividir entre 0")

print(cociente(num1,num2))