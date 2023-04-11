__author__ = "Alfonso Domínguez García"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

lista = [4,56,1,0,-4]

n = len(lista) - 1

def suma_lista_recursiva(lista,n):

    if n == 0:

        return lista[n]

    else:

        return lista[n] + suma_lista_recursiva(lista, n - 1)

print(suma_lista_recursiva(lista,n))


def sumalista2(lista):

    if len(lista) == 0:

        return 0

    else:
        return lista[0] + sumalista2(lista[1::])

print(sumalista2(lista))

print("")

print(__author__)
print(__copyright__)