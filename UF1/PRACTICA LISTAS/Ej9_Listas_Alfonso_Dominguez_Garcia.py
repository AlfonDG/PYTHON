#Crearemos una lista de números vacía
listaNumeros = []

#Ahora le pediremos un número al usuario y este lo añadiremos a la lista.
numero = int(input("Introduzca un número: "))

#Crearemos un bucle WHILE. Hasta que el usuario no introduzca un 0 no parará la secuancia de introducción de números a la lista.
while numero != 0:

    #Le pedimos al usuario varios números hata que introduzca 0 y pararemos la secuancia.
    numero = int(input("Introduzca un número: "))

    #El siguiente paso será añadir los números en la lista.
    listaNumeros.append(numero)

#Mostraremos la lista normal de números introducidos
print("Lista de números sin invertir -> ",listaNumeros,"\n")

#El siguinete paso fuera del bucle será revertir la secuancia de números de tal forma que mostrará los números de forma invertida.
#No es necesario almacenar en una variable la lista de números ya que al usar esta función REVERSE los números se invertirán.
listaNumeros.reverse()

#Mostraremos los resultados de la lista de forma invertida
print("La lista invertida será -> ",listaNumeros)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)
