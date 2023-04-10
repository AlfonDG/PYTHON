#Importamos la libreria de RANDOM
import random

#Creamos la lista de números vacía para añadir los números aleatorios
listaNumerosAleatorios = []

#Crearemos el bucle FOR que nos permita generar los números aleatorios
#Y finalmente los mostraremos por pantalla.
for i in range(0,20):
    #Creamos el rango aleatorio de entre 0 y 9
    numerosAleatorios = random.randint(0,9)
    #Luego los añadiremos a la lista principal los números entre 0 y 9 aleatorios.
    listaNumerosAleatorios.append(numerosAleatorios)
#Mostramos la lista de números aleatorios para ver todos los números del 0 al 9 en un total de 20 posiciones.
print(f"Los números aleatorios son -> {listaNumerosAleatorios}\n")

#Creamos la lista Contador de Números aleatorios, que permitirá contar las N veces que se repite un número en la lista de randoms.
listaContadorNumerosAleatorios = []

#Este segundo bucle FOR permite contar el número de veces que aparece el número N repetidamente
#En la lista de números aleatorios.
for x in range(0,9):
    #En este bucle nos permitirá contar las posiciones y los números que se repite en cada posición de la lista.
    listaContadorNumerosAleatorios.append(listaNumerosAleatorios.count(x))

#A partir de aquí creamos un tercer bucle FOR que nos permitirá recorrer de entre 5 y 10.
randomLen = random.randint(5,10)

#Ahora crearemos el último bucle FOR del ejercicio que nos permitirá repetir este histograma en un número random de entre 5 y 10 veces.
#Se trata de copiar y pegar todos los apartados anteriores y anidarlos en este FOR completo.
for fx in range(randomLen):

    for i in range(0, 20):

        numerosAleatorios = random.randint(0, 9)

        listaNumerosAleatorios.append(numerosAleatorios)

    for x in range(0, 9):
        listaContadorNumerosAleatorios[x] += listaNumerosAleatorios.count(x)

#A partir de aquí crearemos los asteriscos para crear el histograma de asteriscos.
asterisco = "*"

#Finalmnete crearemos el histograma recorriendo la lista contador de números y multiplicando el número de asteriscos por las veces que ha contado el número repetido.
#Por ejemplo multiplicará el número de veces que se repita el 0 por los asteriscos y mostrará la cantidad de asteriscos en total de cada uno de los números.
for yn in range(len(listaContadorNumerosAleatorios)):

    totalAsteriscos = listaContadorNumerosAleatorios[yn] * asterisco

    print(f"{yn}--> {listaContadorNumerosAleatorios[yn]} {totalAsteriscos}")

print("\n")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)