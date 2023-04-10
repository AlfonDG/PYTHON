#Importamos la librería de RANDOM
import random

#Creamos la lista con las 26 posiciones del ABECEDARIO | LA Ñ española no está contemplada en este lista por lo que son 26 posiciones exactas.
listaAbecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Ahora crearemos la lista de Números Aleatorios vacía
listaNumerosAleatorios = []

#Crearé una tercera lista con las palabras resultantes de buscar el número aleatorio y la letra en la posición adecuada.
listaPalabrasAleatoriasResultado = []

#En este bucle FOR crearemos de 0 a 10 un conjunto de números aleatorios del 1 al 26 los dos incluidos, ya que el abecedario son 26 letras.
#Añadiremos a la lista "listaNumerosAleatorios" y ya la tendremos rellenada con los números Aleatorios.
for i in range(0,11):
    numerosAleatorios = random.randint(1,26)
    listaNumerosAleatorios.append(numerosAleatorios)
print(f"La lista de Números aleatorios será -> *{listaNumerosAleatorios}*\n")

#Crearemos en este caso dos bucles. Uno recorrerá la "listaNumerosAleatorios" que generamos anteriormente, en este caso recorrerá los números en cada pasada, es decir
#Recorrerá cada número de la posición. Y el segundo bucle tenemos que hacer un range len de la lista del abecedario para mostrar las posiciones de listasAbecedario
#Y en este caso se hará un condicional que indique si la posición del primer bucle es igual a la posición del segundo bucle. Esto permitirá hacer match de la posición del número y la posición de la letra del abecedario.
#Y añadiré a la "listaPalabrasAleatoriasResultado" las posiciones que hagan match con los números de la lista random de números.
for x in listaNumerosAleatorios:
    for ix in range(len(listaAbecedario)):
        if x == ix:
            listaPalabrasAleatoriasResultado.append(listaAbecedario[x])
print(f"Finalmente devolvemos la lista de 10 posiciones con los valores de las letras del abecedario de forma random -> *{listaPalabrasAleatoriasResultado}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)