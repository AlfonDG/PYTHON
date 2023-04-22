#Ejercicio 1 Lambda

#Crearemos dos variables llamadas num1 y num2 que pedirá dos valores.
num1 = int(input("Introduzca el primer valor: "))

num2 = int(input("Introduzca el segundo valor: "))

'''RESUMEN de las funciones "suma" | "restar" | "multiplicar" y "dividir y el uso de la función LAMBDA:
 
 Las funciones realizan las operaciones artiméticas de sumar,restar,dividir y multiplicar los valores que el usuario introduzca por pantalla
 como son las variables num1 y num2.
 
 Lo importante que realizan todas las funciones es la función lambda: Esta función nos permitirá guardar en cada variable el return de la función lambda
 Es decir, guardaremos el valor de "lambda x,y: x + y" x,y se sustituirá por el valor de num1 y num2.
 
 Realizará lo mismo en el resto de operaciones aritméticas
 Lo importante de esta ejercicio es devolver mediante un return la variable que tengamos almacenada la función de lambda y su operación,
 esta pedirá que en el return devuelva también los valores num1 y num2 que harán referencia a x,y o a y b o la variables que hayamos elegido para sustituir.
 
 Finalmente printamos la función suma(num1,num2) que serán los argumentos de la función principal y tendremos el resultado de nuestra suma, resta, multiplicación y división.
 
 '''

def suma(num1,num2):

    sumaLambda = lambda x,y: x + y

    return sumaLambda(num1,num2)

print(suma(num1,num2))


def restar(num1,num2):

    restaLambda = lambda x,y: x - y

    return restaLambda(num1,num2)

print(restar(num1,num2))

def multiplicar(num1,num2):

    multiplicarLambda = lambda x,y: x * y

    return multiplicarLambda(num1,num2)

print(multiplicar(num1,num2))

def dividir(num1,num2):

    try:

        dividirLambda = lambda x,y: x / y

        return dividirLambda(num1,num2)

    except ZeroDivisionError:

        print("No se puede dividir entre cero, no se mostrará el resultado.")

print(dividir(num1,num2))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)