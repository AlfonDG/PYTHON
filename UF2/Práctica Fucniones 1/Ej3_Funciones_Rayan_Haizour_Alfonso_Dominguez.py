c = str(input("Introduzca la cadena que deseé: "))

n = int(input("Establezca el número de veces que desea repetir la cadena: "))

'''Explicación Ejercicio 3 -> Al mover la función *neteja_pantalla* justamente al inicio de pantalla es que podemos ver que realizamos un total de 25 espacios en blanco 
justo antes de ejecutar la última función dejando así los margenes. Justo al moverlo al final podemos observar que los 25 espacios se harán justo al final de la cadena
no antes.

En caso de mover la llamada de la función *neteja_pantalla* justo al incio teniendo la función al final de todo NO FUNCIONARÁ y mostrará el ERROR:

neteja_pantalla()
NameError: name 'neteja_pantalla' is not defined"

Esto se debe a que no está detectando la estructura de la función debería de llamarse al final de función donde está definida.'''

#Primero definiremos la función tres_linies que permitirá printar tres ineas en blanco. Esto se puede hacer mediante un for que
#Recorra de 0 hasta 3 y printaremos en blanco cada vez.
def tres_linies():

     for i in range(0,3):
        print("")

#En este función realizará mediante un FOR un total de tres líneas más y devolverá las tres anteriores ya que será 3 * 3 lineas.
def nou_lines():

    for i in range(0,3):
        print("")

    return tres_linies()

#La función limpiar pantalla será un bucle FOR que recorrerá que desde 0 a 22
def neteja_pantalla():

    for i in range(0,22):
        print("")

    return tres_linies()

    return nou_lines()

#Préviamente mostraremos la función neteja_pantalla() y esto realizará los espacios en blanco de las funciones anteriores.
neteja_pantalla()

#Aquí generaremos la función concatena N veces que pasará los parámetros c y n (c será la cadena que el usuario haya introducido) y
#(n será el número de veces que desea que se repita esta cadena)
def concatena_n_vegades(c,n):

    #Para poder realizar esto haremos un for desde 0 hasta N veces que se repita esta cadena.
    for i in range(0,n):
        print(c)

#Finalmente llamamos a la función sin print ya que realizamos uno en la función y podría devolver NONE.
concatena_n_vegades(c,n)

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)


