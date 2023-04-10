__author__ = "Bilal & Alfonso"
__copyright__="Copyright © 2023 Bilal & Alfonso"

#Creamos la función suma que pase como parámetro un conjunto de argumentos, en este caso un diccionario.
def suma(**kwargs):

    #Creamos una variable sumaElementosDiccionario la seteamos a 0. Lo que significa que tendremos una variable acumulador a 0
    #Aquí añadiremos el resultado de la suma de los valores del diccionario.

    sumaElementosDiccionario = 0

    #Ahora creamos un bucle FOR que permita recorrer todos los valores que le hayamos pasado manualmente
    #Esto permitirá añadir a la sumaElementosDiccionario los valores y acumular la suma de los mimsos en una variable.
    for valores in kwargs.values():

        if puede_sumar(valores) == True:

            sumaElementosDiccionario += valores

    #Finalmente devolvemos el resultado en un return de la función suma.
    return "La suma de todos los valores es igual a -> ",sumaElementosDiccionario

#Ahora crearemos la segunda parte del ejercicio, que nos permitirá realizar una función que compruebe que los valores se pueden sumar
#De esta forma realizará la comporbación conforme si los valores son aptos para la suma.
#Es decir podemos comporbar que los valores que le pase el usuario de forma manual son INT o FLOAT, si son ambos podrá realizar la operación
#De lo contrario no funcionará y lanzará una excepción de código.
def puede_sumar(todosValoresKwargs):

    #Almacenamos todo el contenido de la función dentro de un try y except de tal forma que podrmeos gestionar los errores mejor
    try:

        #En este condicional lo que haremos será comprobar que todos los valores sean o INT o FLOAT, si es así devolverá un True para poder continuar con las operaciones
        #De lo contrario no podrá continuar y devolverá un TypeError conforme no ha escrito si es INT or FLOAT.
        if type(todosValoresKwargs) == int or type(todosValoresKwargs) == float:

            return True

        #Aquí devolverá el error de TypeError y debería de devolver de forma correcta la raise TypeError o bien Excepcion.
        else:
            raise TypeError

    except TypeError:
        print(f"El valor NO se puede sumar, NO son INT o bien FLOAT por lo que no continuaremos la ejecución del código.")
        exit()

print(suma(valor1 = 5, valor2 = 7, valor3 = 20, valor4 = 2, valor5 = 6))

print("")

print(__author__)
print(__copyright__)
