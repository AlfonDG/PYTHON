def mayor_tres_numeros(*args):

    listaNumeros = []

    for i in args:

        listaNumeros.append(i)

    maximoNumero = max(listaNumeros)

    return maximoNumero

print(mayor_tres_numeros(3,5,9))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)