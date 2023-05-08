lista = [2,2,3]

def sumaElementos(lista):

    if len(lista) == 0:

        return 0

    else:

        return lista[0] + sumaElementos(lista[1:])

print(sumaElementos(lista))