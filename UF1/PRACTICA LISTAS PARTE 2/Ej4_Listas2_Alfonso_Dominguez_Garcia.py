#Primero IMPORTAMOS la librería RANDOM
import random

#Crearé la lista de números aleatorios vacía
listaNumerosAleatorios = []

#El siguiente paso será rellenar el array de números aleatorios en un rango de 0 a 21 y de esta forma crearemos una array de números aleatorios de 0 a 20
#Luego debemos de crear una variable que guardará los números aleatorios usando un random.randint que va de 0 a 9 incluidos.
for i in range(0,20):

    numerosAleatorios = random.randint(0,9)

    listaNumerosAleatorios.append(numerosAleatorios)

print(f"La lista de números aleatorios es -> {listaNumerosAleatorios}")

#Ahora toca la segunda parte del ejercicio que será crear la lista de Distancias
listaDistancias = []

#Aquí crearemos
for n in range(len(listaNumerosAleatorios)):

    listaDistancias.append(listaNumerosAleatorios[n])

#En este bucle nos pedirá rellenar la lista de las distancias entre 0 y 9. Pero será la principal de la secuancia. Solamente servirá para añadir las distancias a la lista
#Pero NO acumulará los números.
for nx in range(0,9):
    print(f"\nlistaDistancias[{nx}] = ",end="")
    for fx in range(len(listaDistancias)):
       if fx == len(listaDistancias)-1:
           print(f"|{nx}-{listaDistancias[fx]}| ", end="")
       else:
           print(f"|{nx}-{listaDistancias[fx]}| + ", end="")
print("\n\n****En este punto es una lista de ejemplo***")

#Crearemos la variable que permita recorrer un random de entre 5 y 10
randomLen = random.randint(5,10)

#Crearemos el último bucle FOR que permitirá realizar los dos bucles anteriores anidados pero esta vez acumulará en la lista distancias.
#En este caso mostrará acumulada las distancias a su vez recorridas en la listaDistancias.
for f in range(randomLen):

    for n in range(len(listaNumerosAleatorios)):
        listaDistancias.append(listaNumerosAleatorios[n])

    for nx in range(0, 9):
        print(f"\nlistaDistancias[{nx}] = ", end="")
        for fx in range(len(listaDistancias)):
            if fx == len(listaDistancias) - 1:
                print(f"|{nx}-{listaDistancias[fx]}| ", end="")
            else:
                print(f"|{nx}-{listaDistancias[fx]}| + ", end="")

        for fx in range(len(listaNumerosAleatorios)):
            listaDistancias[fx] += listaNumerosAleatorios[fx]
    print("")

print("\n")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)
