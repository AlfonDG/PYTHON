#Ejercicio número 4 del módulo de Lambda

#Primero crearemos una lista de valores incluyendo el valor 1312. Esta función lo que realizará será
#Buscar en toda la lista el valor de X que supere 1312 (tal y como indica el enunciado).
'''Los valores de esta lista pueden ser modificados para comprobar que el ejercicio funciona correctamente.'''
listaValoresLambda = [1000,5000,50,1312,25,2000]

#Ahora crearemos la función que he denominado "filtrado_valores_lista_lambda" la cual tendrá el argumento (listaValoresLambda)
#Una vez hecho esto lo que haremos será crear la función lambda que guadaré en una variable que se llamará "filtrarValores"
#La función de lambda lo que hará será usar el método list(filter) que permitirá filtrar va,ores en la lista y permitirá recorrerla
#La variable x comprobará que sea superior 1312 de mi lista de valores, entonces devolverá los valores superiores.

#Finalmente realizaremos un return de la variable "filtrarValores" que permitirá devolver la función con los valores superiores de la lista.
#Printamos la función entrea que tenía como parámetros la lista de valores.
def filtrado_valores_lista_lambda(listaValoresLambda):

    filtrarValores = list(filter(lambda x: x > 1312,listaValoresLambda))

    return filtrarValores

print(filtrado_valores_lista_lambda(listaValoresLambda))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)