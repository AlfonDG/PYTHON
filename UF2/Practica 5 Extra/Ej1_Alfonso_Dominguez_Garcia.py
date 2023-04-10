__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

#Primero establecemos el valor del contador a 0. Tal y como nos indica el ejercicio
contador = 0

#Luego debemos de establecer una variable que permitirá ejecutar este código en bucle el número de veces que el usuario deseé
numVecesRepetir = int(input("Introduzca el número de veces que desea llamar a la función: "))

#Ahora creamos la función incrementar_comptador. Lo que permitirá es tener una variable global que hará referencia a contador.
#De esta forma lo que estamos haciendo es que si deseamos modificar esta variable desde la misma función también se modificará de forma local o fuera
#De la función.

def incrementar_comptador():

    global contador

    #Aquí sumamos al contador + 1 para que cada vez que ejecute esta función el usaurio reciba un mensaje del número de vecees que se ha ejecutado
    #Esta función.

    contador += 1

    return "Ha llamado a la función un total de -> " ,contador, "veces"

#Aquí es donde he creado el bucle While que permitirá ejecutar en loop hasta llegar a 0 y de esta forma ejecutará la llamada a la función anterior
#Se repetirá el número de veces que el usuario haya establecido.
while numVecesRepetir > 0:

    print(incrementar_comptador())

    #Decremento del bucle While hasta llegar a 0 en base al valor introducido por el usuario anteriormente.
    numVecesRepetir -= 1

print("")
print(__author__)
print(__copyright__)