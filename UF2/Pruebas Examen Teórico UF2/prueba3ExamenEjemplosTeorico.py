lista = [3,4,8,25,2,10,5,-10]

def metodo_burbuja_lista(lista):

    for i in range(len(lista)):

        for j in range(len(lista) - 1):

            if lista[j] > lista[j + 1]:

                auxiliarNumeros = lista[j]

                lista[j] = lista[j+1]

                lista[j + 1] = auxiliarNumeros

    return lista

print(metodo_burbuja_lista(lista))