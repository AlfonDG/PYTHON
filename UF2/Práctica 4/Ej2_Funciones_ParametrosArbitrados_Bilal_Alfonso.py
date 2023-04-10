__author__ = "Bilal & Alfonso"
__copyright__="Copyright © 2023 Bilal & Alfonso"

#Crearemos una función que permita pasar como parámetros dos valores enteros naturalaes, un conjunto de argumentos a continuación *args
#Luego también pasamos finalmente los **kwargs que será el diccionarios de elementos a multiplicar.
def funcion(a,b,*args,**kwargs):

    #Seteamos la variable de multiplicacionValores a 1 de tal forma que si fuese 0 no multiplicaría los valores el resultado sería siempre 0
    multiplicacionValores = 1

    #Recorremos primero los valores del diccionario y los vamos multiplicando los valores en el acumulador es decir 1 *10 * 30 * 20 etc...
    for valoresKwargs in kwargs.values():

        #Este condicional permite observar si la función de puede multiplicar valorará si no ha saltado un raise exception o en este caso TypeError
        #De ser así no continuará con el código
        if puede_multiplicar(valoresKwargs) == True:

            multiplicacionValores *= valoresKwargs

    #Ahora recorremos los argumentos. Con lo que nos permitirá multiplicar en el mismo acumulador los valores que se pasen como args, justo los que sona continuación de a y b como argumentos
    #Comprobaremos con otro IF igual que hemos realizado arriba para comporbar que los valores de *arg son completamente válidos. Ni FlOATS o Strings.
    for valoresArgs in args:

        if puede_multiplicar(valoresArgs) == True:

            multiplicacionValores *= valoresArgs

    #Finalmente multiplicamos al final los valores de los argumentos a y b respectivamente. Acumulamos ambos valores ya.
    multiplicacionValores *= a

    multiplicacionValores *= b

    #Y finalmente devolvemos con un return los valores de la multiplicación y el resultado final con la ejecución de código.
    return "Todos los valores multiplicados serán iguales a -> ",multiplicacionValores

def puede_multiplicar(todosValoresKwargs):

    #Almacenamos todo el contenido de la función dentro de un try y except de tal forma que podrmeos gestionar los errores mejor
    try:

        #En este condicional lo que haremos será comprobar que todos los valores sean o INT o FLOAT, si es así devolverá un True para poder continuar con las operaciones
        #De lo contrario no podrá continuar y devolverá un TypeError conforme no ha escrito si es INT or FLOAT.
        if type(todosValoresKwargs) == int:
            return True

        else:
            raise TypeError

    except TypeError:
        #Aquí devolverá el error de TypeError y debería de devolver de forma correcta la raise TypeError o bien Excepcion y saldremos mediante un exit().
        print("El valor NO se puede multiplicar, no son INT por lo que no podremos ejecutar el siguiente código.")
        exit()

print(funcion(10,30,20,2,valor1 = 3,valor2 = 9,valor3 = 6))

print("")

print(__author__)
print(__copyright__)