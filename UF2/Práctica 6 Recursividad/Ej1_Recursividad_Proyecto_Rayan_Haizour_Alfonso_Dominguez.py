a = int(input("Introduzca el valor de A: "))

b = int(input("Introduzca el valor de B: "))

print("")

titulo_tabla = "TABLA MÉTODO RUS".center(20)

margenes = "—" * 20

print(titulo_tabla)

def metode_rus(a,b):

    #Aquí hemos creaod una pequeña tabla para mostrar el reusltado de los valores de A y B + resultado final que será el final resultado
    #De la función recursiva. Pasaremos a str() los números de tal forma que podamos centrarlos.

    centrarA = str(a)

    centrarB = str(b)

    print("A   ->  " + centrarA.center(10))

    print("B   ->  " + centrarB.center(10))

    print(margenes)

    #Si la variable a es == 1 devolvemos la variable b. Esto se podría traducir que si el número de A es 1 devuelve el número actual de B.
    #Une jemplo sería al realizar que A -> 27 y B -> 82 pues cuando A sea 1 en las iteraciones recursivas pues B será igual a 1312 finalmente.

    if a == 1:

        return b

    #En este condicional lo que importa es comprobar que el número a sea múltiplo de 2 == 0 por lo tanto si el número es par
    #NO sumará los números en la tabla SUMA del método Ruso. Es decir que solamente si B es impar los sumará y decremenatrá la variable A hasta llegar al final.

    #En este caso se dividirá A hasta llegar a un número menosr o 1 al final y por otro lado multiplicará * 2 b.

    elif a % 2 == 0:

        return metode_rus(a // 2, b * 2)

    #De lo contarrio si el número que ha establecido el usuario es impar se devuelve la suma de b + metodo_ruso recursivo que contará
    #Que los números impares se suman y la variable A continua decrementando en la divisón entre 2 y b siguie incrementando multiplicando * 2
    #Con la diferencia de que este valor se sumará b para obtener el resultado de la SUMA final.

    else:

        return b + metode_rus(a // 2, b * 2)

#Aquí imprimimos el formato de table final con el resultado de todas las operaciones.
print(margenes)
print("Resultat: ",metode_rus(a,b))
print(margenes)

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)