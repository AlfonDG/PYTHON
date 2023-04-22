#Ejercicio número 2

#Primero creamos una variable que permita pedir un valor y ver si el valor es par o impar.

num = int(input("Introduzca el valor de num y te diré si el número es par o impar: "))

#Ahora crearemos una función llamada "numero_par_impar_lambda" y de esta forma le pasaremos como parámetro el valor de "num".
def numero_par_impar_lambda(num):

    #Guardaremos el valor de la función lamda para saber si el valor que ha introducido el usuario es PAR o IMPAR.
    #Devolverá un return de TRUE o FALSE más el mensaje explicado más abajo.
    saberParLambda = lambda x: x % 2 == 0

    #Crearemos un condicional que permita indicar que si el valor de num es PAR mostrará el mensaje en el return + el return de la propia función lamda
    #De esta forma devolverá el return de la función lambda anterior que será TRUE si es PAR o FALSE si es IMPAR.
    if num % 2 == 0:

        return "El número es par", saberParLambda(num)

    else:
        return "El número es impar", saberParLambda(num)

#Printamos toda la función principal con el argumento "num".
print(numero_par_impar_lambda(num))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)