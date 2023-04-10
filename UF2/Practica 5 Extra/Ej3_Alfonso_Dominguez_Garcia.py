__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

#Primero iniciamos la variable total a 0 tal y como indica el ejercicio
total = 0

#ahora establecemos el número de veces que desea repetir que se ejecute la función.
n = int(input("Introduzca N veces que desea repetir el código: "))

#Ahora crearemos la función agregar_numero que tendrá como prámetro n y que según el ejercicio querrá que se modifique el valor de total
#A total += n de tal forma que se irá añadiendo a la variable de total la suma de veces que desea repetir la función.

def agregar_numero(n):

    #establecemos la palabra reservada como global y de esta forma modificaremos el valor de la variable total.
    global total

    #En este caso se formateará el valor de la variable "total" pero no interferirá en el bucle loop WHILE.
    #Ya que cuando acabe el loop este dejará de repetir la secuencia de valores.
    total += n

#Aquí establecemos el bucle WHILE de tal forma que repetirá la función N veces que el usuario haya establecido.
while n > 0:

    agregar_numero(n)

    #Decrementamos el valor de n hasta llegar a 0 de tal forma que al llegar a 0 el bucle WHILE dejará de entrar en la función "agregar_numero".
    n -= 1

print(total)

print("")
print(__author__)
print(__copyright__)