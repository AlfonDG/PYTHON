
f = int(input("Introduce el valor para la función de Fibonacci: "))

def fibonacci(f):

    if f == 0:

        return 0

    elif f == 1:

        return 1

    else:
        return fibonacci(f - 1) + fibonacci(f - 2)

#Comprobación de Fibonacci como puede recorrer y ver la sucesión.
for i in range(10):
    print(i,"->",fibonacci(i))