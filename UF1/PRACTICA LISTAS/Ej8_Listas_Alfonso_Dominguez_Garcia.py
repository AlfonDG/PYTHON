#Primero le pediremos un número al usuario del 1 al 10.
numero = int(input("Introduzca el número que desee y la daré su table de multiplicar: "))

#Crearemos la lista con la tabla de multiplicar y con los valores multiplicados.
listaTablaMultiplicar = []

#Si el número supera 10 no continuará con el programa. El enunciado dice de 1 hasta 10 no de 0 o -1 o 11 en adelante.
if numero > 10 or numero <= 0:
    print("Pararemos el código. Has escrito un número mayor de 10 o has establecido un valor igual a 0")

#De lo contarrio haremos un bucle FOR que recorrerá en un rango del 0 a 11 en este caso 0 cuenta como una posición por lo que será 10.
else:
    #Finalmente lo que hará será crear una variable con el resultado de la multiplicación y lo añadiremos a la lista.
    for i in range(0,11):

        resultadoMultiplicar = i * numero

        listaTablaMultiplicar.append(resultadoMultiplicar)

    print(listaTablaMultiplicar)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)