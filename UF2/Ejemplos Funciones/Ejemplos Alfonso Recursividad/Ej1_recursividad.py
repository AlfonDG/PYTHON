
n = int(input("Introduzca el valor del número que desea saber su factorial: "))

def factorial_numero(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial_numero(n - 1)

print(factorial_numero(n))