#Primero importamos el módulo Random.
import random

#Usando el módulo Random debemos de crear una variable que contendrá un número aletarorio entre 0 y 1000 ambos números incluidos gracias a randint
numAleatorio = random.randint(0,1000)

#Aquí printamos el valor para poder o intentar adivinar el número. Este print es solamente para realizar las pruebas
print(numAleatorio)

#Una variable contador seteada a 0 permitirá contar el número de veces o intentos que realizará el usuario
contadorVeces = 0

#Ahora creamos el cuerpo del ejercicio, una función que la hemos denominado "endevinar_num_aleatori" que tendrá como parámetros 4 variables
#El número aleatorio del 0 a l 1000, luego el contador de intentos, el número mínimo que nos permitirá contar el valor mínimo de la variable Random
#En este caso cuando se pase la función se añadirá el valor de 0 y la variable numMaximo que nos permitirá saber el valor de 1000 que será el valor máximo
#Del número random.
def endevinar_num_aleatori(numAleatorio,contadorVeces,numeroMinimo,numeroMaximo):

    #Le pediremos al usuarios que introduzca un valor de entre 0 y 1000 obligatoriamente.
    numAdivinar = int(input("Qué número cres que es?."))

    #Cada vez que se ejecute el código se sumará al contador de intentos + 1 para contar todos los intentos hasta adivinar el número.
    contadorVeces += 1

    #Aquí se printa el rango que mostrará el valor del número mínimo y el número máximo (estos valores serán modificables a medida que el usuario vaya estableciendo los números)
    #Dará pistas de si se encuentra en el rango.
    print(f"{numeroMinimo} - {numeroMaximo}")

    #Primer condicional: Si el número que ha introducido el usuario no se encuentra entre 1000 o bien inferior a 0 saldrá del programa
    #Ya que los valores no se encuentran en el rango.
    if numAdivinar > 1000 or numAdivinar < 0:

        return "Lo sentimos, pero no ha establecido un número que esté dentro del rango. Saliendo del programa..."

    #Este condicional solamente se ejecutará: CASO BASE si el usuario consigue adivinar el valor que se encuentra dentro del rango y que ha generado aleatoriamente.
    elif numAleatorio == numAdivinar:

        return f"CORRECTO. Has adivinado el número en el intento número {contadorVeces}"

    #El siguiente condicional: RECURSIVIDAD nos permite mostrar el valor mínimo que será el valor que el usuario ha establecido y el número máximo
    #Luego el número mínimo en este claso se seteará por numAdivinar que en este caso será el número que introduzca el usuario y si el número adivinar es inferior
    #Es inferior a el número que ha introducio el usuario deberá de aumentar su valor y mostrará el rango actual y le diremos al usuario que deberá de introducir un número superior al que ha establecido
    elif numAdivinar < numAleatorio:

        numeroMinimo = numAdivinar
        print(f"El número se encuentra entre {numeroMinimo} y {numeroMaximo}, por debajo del valor {numeroMaximo} deberá aumentar su valor")

        return endevinar_num_aleatori(numAleatorio,contadorVeces,numeroMinimo,numeroMaximo)

    #Ahora a la inversa, si el número que es random es superior al número que ha introducido el usuario deberemos de setear el valor máximo al número que ha esteblecido el usuario
    #Y le diremos al usuario el valor de rango y que tendrá que disminuir el valor que ha establecido y de esta forma daremos la pista de que el usuario ha superado el valor máximo en aquel momento.
    elif numAdivinar > numAleatorio:

        numeroMaximo = numAdivinar
        print(f"El número se encuentra entre {numeroMinimo} y {numeroMaximo}, por encima de {numeroMaximo} deberá bajar el valor")
        #print(f"El número se encuentra por debajo de {numeroMaximo}")

        return endevinar_num_aleatori(numAleatorio,contadorVeces,numeroMaximo,numeroMinimo)

#Ahora devolvemos la función final añadiendo el 0 y el 1000 que hará referencia a las variables numMinimo y numMaximo.
print(endevinar_num_aleatori(numAleatorio,contadorVeces,0,1000))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)