lista = [27,3,4,5,16,6,8,6]

def metodo_burbuja(lista):

    for i in range(len(lista)):

        for j in range(len(lista)-1):

            if lista[j] > lista[j + 1]:

                #lista[j], lista[j + 1] = lista[j + 1], lista[j]

                auxiliar = lista[j]

                lista[j] = lista[j + 1]

                lista[j + 1] = auxiliar
    return lista

print(metodo_burbuja(lista))