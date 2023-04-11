
#Si el valor de N es 0 no se ejecuta, es decir entrará en la función y esta vez se quedará en 1 no en 0.
n = 0

def factorial_n(n):

    resultado = 1

    for i in range(2,n + 1):

        resultado *= i

    return "El factorial del resultado será -> ",resultado

print(factorial_n(n))