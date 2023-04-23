#Ejercicio 1

'''EXPLICACIÓN EJERCICIO Nº 1
------------------------------------------------------------------------------------
Primero introducido la variable de numVeces que nos permitirá establecer el número máximo de veces que deseamos que se
repita la secuancia de valores.

Luego le pediremos al usuario el valor de N que será el número que repetirá la secuencia hasta fializar el valor de a, es decir,
según la siguiente fórmula que nos muestra el ejercicio -> funcio_recursiva { if n == 1 | 6 elif n > 1 | 1/2 * funcio_recursiva(n-1) + 4
si N es por ejemplo 10 que será igual al valor de N pues devolverá un único valor en pricipio que será = 7.99609375

Si embargo, nosotros queremos mostrar la secuancia de valores: Para ello lo que hacemos es un bucle FOR que recorrerá desde 1 ya que el valor de 0
será return de N = 1 y variable A = 6 (A más adelante será seteada como la vuelta de la función recursiva).

Por lo que el bucle FOR se recorrerá hasta llegar a numVeces.

El siguiente paso que es el que he explicado anteriormente será que setearemos la variable de A = funcio_recursiva(i) y como argumento
recibirá el valor de i: Esto se debe a que i es el número de veces que recorrerá el bucle y su repetición/llamada a la función [fucnio_recursiva]

Y finalmente printamos el valor de f"n= {i}, a={a}" de tal forma que uno muestra los números 1,2,3,4,5,6,7.... etc hasta llegar al valor de numVeces
y el otro valor de a será sustituido cada vez por la llamada a la función recursiva para su secuencia.
------------------------------------------------------------------------------------
'''


numVeces = int(input("Introduzca el número de veces que deseé ejecutar el código: "))

n = int(input("Introduzca el valor de N: "))

def funcio_recursiva(n):

    if n == 1:

        return 6

    elif n > 1:

        return 1/2 * funcio_recursiva(n - 1) + 4

print(funcio_recursiva(n))

for i in range(1, numVeces + 1):

    a = funcio_recursiva(i)

    print(f"n= {i} , a= {a}")

# Ejercicio 2

'''EXPLICACIÓN EJERCICIO Nº 2
----------------------------------------------------------------------------------
 Primero crearé un bucle FOR que permitá pedidr al usuario cada valor de la lista 1 y lista 2, con lo que el usuario irá
 rellenando el arreglo de forma automática y podrá escoger los valores que deseé.
 
 El siguinete paso será ejecutar la función "llistes_recursives_comparacio". Este código lo que hace es comporbar que la longitud de
 la lista 1 y de la lista 2 sean diferentes. Si se cumple este caso devolverá un FALSE como valor de salida y terminará el programa.
 
 El siguinete condicional mira que ambas listas coincidan en que su longitud sea exacta. Si es así mostrará el mensaje que dirá
 
-> ""Ambas listas coinciden sus valores en las mimas posiciones""

El más importante es que si en el segundo caso se cumple pasará al else final que permitirá saber que si los valores de 
las posiciones 0 de ambas lisas son exactamente iguales/mismos valores, devolverá una función recursiva que permitirá recorrer los valores
uno por uno hasta saber si coincidenc en ambas listas. Si es así como el segundo condicional muestra el mismo mensaje 
pues lo mostrará si se cumple también en la recursión. 
------------------------------------------------------------------------------------
'''

lista1 = []

lista2 = []

numVecesAnadirLista = int(input("\nIntroduzca el número de veces que desea añadir valores a la lista1 y lista2: "))

for i in range(0, numVecesAnadirLista):

    elementoLista1 = int(input("\nIntroduzca el valor para lista1: "))

    elementoLista2 = int(input("Introduzca el valor para la lista2: "))

    lista1.append(elementoLista1)

    lista2.append(elementoLista2)

print(lista1, lista2)

print("\n")

def llistes_recursives_comprobacio(lista1, lista2):

    if len(lista1) != len(lista2):

        return False

    elif len(lista1) == 0 and len(lista2) == 0:

        print("Ambas listas coinciden sus valores en las mimas posiciones")

        return True

    else:

        return lista1[0] == lista2[0] and llistes_recursives_comprobacio(lista1[1::], lista2[1::])


print(llistes_recursives_comprobacio(lista1, lista2))

print("\n")

#Ejercicio 3

'''EXPLICACIÓN EJERCICIO Nº 3
------------------------------------------------------------------------------------------------------------------------
El ejercicio número 3 constará de una lista vacía el cual permitirá al usuario añadir un número máximo que deseé
y dentro de un Bucle FOR recorrerá el bucle hasta llegar al valor máximo que había establecido el usuario, una vez hecho esto
se añadirán los valores a la lista.

Ahora la función lo que hará será extraer el valor máximo de una lista. Para ello haremos un caso base que diga que si la len(lista) o longitud
de la lista sea igual a 1 devolveremos todos los valores de la lista ya que a cada pasada de la recursión pasará por los valores uno a uno.
Al finalizar la recursión.

El primer condicional devolverá todos los valores en caso de que la len(lista) se igual a 1. Como esta función se acabará cumplieando, ya que
la función recursiva recorrerá los valores hasta llegar al último valor que es 1 al principio. Si fuese 0 devolvería error conforme el índice ha sido superado
y si es 2, 3 o superior solamente mostrará el último valor más grande. Es decir, en una lista de valores [4,5,8,9] si se ha establecido en el condicional el valor 3
mostrará 8 como valor superior sin contar el 9 que se encuentra en la posición 4.

Mediante la función max(lista[0] o lista de todos los valores en la misma lista y la recursión que recorrerá todos los valores uno por uno)
y extraerá el valor más grande de la lista.
------------------------------------------------------------------------------------------------------------------------
'''

lista = []

numVeces = int(input("\nIntroduzca la cantidad de valores que desea añadir a la única lista: "))

for i in range(0, numVeces):

    numero = int(input("Introduzca el número en la lista: "))

    lista.append(numero)

print(lista)


def calcul_numero_mes_gran(lista):

    if len(lista) == 1:

        return lista[0]

    else:

        return max(lista[0], calcul_numero_mes_gran(lista[1:]))

print(calcul_numero_mes_gran(lista))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)