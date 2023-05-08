listaEnteros = [5,8,2,1,4,11]

def sumar_numero_pares(listaEnteros):

    sumaValores = 0

    try:

        for i in listaEnteros:

            if i % 2 == 0:

                sumaValores += i

        return sumaValores

    except TypeError:

        print(f"Uno de los elementos no es integer")

print(sumar_numero_pares(listaEnteros))