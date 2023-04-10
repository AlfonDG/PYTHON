lista = []#Primero creamos la lista vacía
#Aquí le pediremos al usuario que introduzca el número de veces que desea introducir nombres
numeroVeces = int(input("Escriba el número de nombres que desea insertar: "))

#Crearemos una variable que será ContadorVeces hasta llegar a 0 de esta forma pararemos el bucle.
contadorVeces = numeroVeces

#Crearemos el bucle While que hasta que el contador de veces no llegue a 0 no parará de pedir nombres a la lista
while contadorVeces > 0:

    nombre = str(input("Escriba el nombre: "))

    #Añadiremos los nombres introducidos a la lista
    lista.append(nombre)

    #Restamos al contador de veces -1 hasta que llegue a 0
    contadorVeces -= 1

#Finalmente printamos la lista con los resultados de los nombres.
print(lista)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)