__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

#Primero iniciamos la variable total a 0 tal y como indica el ejercicio
total = 0

#ahora establecemos el número de veces que desea repetir que se ejecute la función.
numVeces = int(input("Introduzca N veces que desea repetir el código: "))

#Ahora crearemos la función agregar_numero que tendrá como prámetro n y que según el ejercicio querrá que se modifique el valor de total
#A total += n de tal forma que se irá añadiendo a la variable de total la suma de veces que desea repetir la función.

def agregar_numero(n):

    #establecemos la palabra reservada como global y de esta forma modificaremos el valor de la variable total.
    global total

    #En este caso se formateará el valor de la variable "total" pero no interferirá en el bucle loop WHILE.
    #Ya que cuando acabe el loop este dejará de repetir la secuencia de valores.
    total += n

#Aquí establecemos el bucle WHILE de tal forma que repetirá la función N veces que el usuario haya establecido.
while numVeces > 0:

    #aquí pedimos los números que desean sumar para la función.
    n = int(input("\nIntroduzca el valor que desea llamar a la función: "))

    #Llamamos a la función "agregar_numero(n)" que ejecutará el código N veces que el usuario haya establecido.
    agregar_numero(n)

    #Decrementamos el valor de n hasta llegar a 0 de tal forma que al llegar a 0 el bucle WHILE dejará de entrar en la función "agregar_numero".
    numVeces -= 1

#Finalmente y más importante printalos la variable "total" ya que contiene los valores de la suma de n añadidas a la variable global "total".
print(total)

print("")
print(__author__)
print(__copyright__)