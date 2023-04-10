#Establecemos y definimos un total de tres listas.
lista1 = []

lista2 = []

listaResultado = []

#Añadimos dos variables para establecer cuántos valores máximos queremos meter en la lista. Tanto lista 1 como lista 2 su máximo de valores a introducir:
valorMaximoLista1 = int(input("Introduzca el valor máximo de la lista 1: "))

valorMaximoLista2 = int(input("Introduzca el valor máximo de la lista 2: "))

#Ahora crearemos un While prévio que lo que hará será que hasta que las variables máximas de valores sean 0 continuará y no parará
#Por eso son variables contadores que iremos restando hasta finalizar ambos Whiles. Hemos preferido separarlo para que se vea mejor como se gestiona.
while valorMaximoLista1 > 0:

    valorParaLista1 = int(input("\nIntroduzca el valor a añadir a la lista nº 1: "))

    lista1.append(valorParaLista1)

    valorMaximoLista1 -= 1

while valorMaximoLista2 > 0:

    valorParaLista2 = int(input("\nIntroduzca el valor a añadir a la lista nº 2: "))

    lista2.append(valorParaLista2)

    valorMaximoLista2 -= 1

#Ahora definimos la función y pasamos las dos listas como parámetros de la función con los valores ya introducidos
def listasEj2(lista1,lista2):

    #Ahora crearemos un bucle FOR que recorrerá la lista1 y comprobará los valores que hay dentro de ambas listas.
    #Si encontramos el valor de lista1 en lista2 lo añadiremos en listaResultado. No sin antes ver que en lista1[i] (Valor de lista1)
    #NO se encuentra ya añadida en la lista... De esta forma evitaremos repetir los valores a la lista.
    for i in range(len(lista1)):

        if lista1[i] in lista2 and lista1[i] not in listaResultado:

            listaResultado.append(lista1[i])
    #Finalmente devolvemos el resultado listaResultado que será la lista con los valores que el usuario haya repetido en ambas listas.
    return listaResultado

#Finalmente printamos el resultado de la función con ambos parámetros introducidos.
print(listasEj2(lista1,lista2))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)