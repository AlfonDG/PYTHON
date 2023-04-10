#Creamos la lista de números vacía
listaNumeros = []

#Pedimos al usuario introducir el número que desee el usuario.
numerosIntroducir = int(input("Introduzca un número, no pararemos hasta que introduzca -1: ")) #Esta variable iniciada a 0 al ser difernete a -1 entrará en el bucle While y podremos añadir números a la lista, este no contará como un número más en la lista.

#Ahora establecemos la variable de suma a 0 para ir acumulando la suma de todos los valores al final
sumaNumerosLista = 0

#Crearemos un bucle WHILE que permita que hasta que el usuario no escriba -1 no pararemos de pedir números
while numerosIntroducir != -1:

    #Introducimos primero el primer número, es decir que el primer número que el usuario haya puesto ya cuente como 1.
    #Y luego vaya añadiendo los demás
    listaNumeros.append(numerosIntroducir)

    #Mediante la funbción SUM(lista) permitirá sumar todos los valores de una lista y yo lo he guardado en una variable.
    sumaNumerosLista = sum(listaNumeros)

    #Le seguiremos pidiendo números al final al usuario hasta que escriba -1 y dejaremos de añadir números.
    numerosIntroducir = int(input("Introduzca un número, no pararemos hasta que introduzca -1: "))

#Finalmente realizamos la operación de la suma de todos los números entre la longitud de la lista.
#De esta forma tendremos la operación de la MEDIA de todos los números
resultadoMediana = sumaNumerosLista / len(listaNumeros)

#Printamos el resultado.
print(f"Lista -> *{listaNumeros}* La suma de todos los números en la lista será *{sumaNumerosLista}* y la mediana de todos los números será *{resultadoMediana}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)