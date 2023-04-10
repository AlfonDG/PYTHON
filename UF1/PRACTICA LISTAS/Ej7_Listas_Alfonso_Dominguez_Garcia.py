#Creamos la primera lista de palabras
listaPalabras = []

#Creamos la segunda lista de palabras
segundaLista = []

#Ahora creamos la variable de parada del bucle, en caso de que el usuario escriba *si/no* parará el bucle WHILE.
pararBucle = "no"

#Crearemos un bucle WHILE que hasta que no se introduzca *si* no parará el bucle
while pararBucle != "si":

    #Introducimos la palabra que desee el usuario.
    cadena = str(input("Introduzca la palabra: "))

    #Ahora añadiremos la cadena a la lista.
    listaPalabras.append(cadena)

    #Le pediremos al usuario si deseamos parar el bucle.
    pararBucle = str(input("Desea parar el bucle? Escriba si/no: "))

    #En caso de que el usuario quiera parar el bucle. Dejará de introducir cadenas.
    if pararBucle == "si":

        #Guardaremos en una variable la lista pero invertida
        listaPalabrasInvertidas = listaPalabras[::-1]

        #En este caso lo que haremos será añadir las cadenas invertidas en una segunda lista
        #Lo que haremos será invertir la lista y añadiremos a la segunda lista la cadena de forma invertida sin necesidad de usar la función REVERSE()
        segundaLista.append(listaPalabrasInvertidas)

        #Printaremos los resultados.
        print(f"La lista de cadenas introducidas será -> {listaPalabras}")

        print(f"\nFinalmente la lista invertida con las cadenas será -> {segundaLista}")

    #De lo contrario seguiremos pidiendo números al programa.
    else:
        print("Continuaremos con el programa")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)