#Inicializamos una variable contador a 0
contador = 0

#Le pedimos al usuario la cantidad de números que desea introducir.
cantidadNumeros = int(input("Escriba la cantidad de números: "))

#Crearemos la variable acumulador a 0 y de esta forma
acumuladorNumGrande = 0

#En el bucle lo que haremos será que mientras que el contador sea inferior a la cantidad máxima de números pues entre en bucle constanetmente
while contador < cantidadNumeros:

    #Le pedimos al usuario que introduzca los números hasta llegar al límite introducidos
    num = int(input("Escriba los números: "))

    #Contamos los números de 1 en 1
    contador += 1

    #Si el contador es inferior al número que el usuario haya metido por teclado entonces lo añadiremos a la variable de acumulador
    if num > contador:
        acumuladorNumGrande = num

#El número más grande será... Le mostramos al usuario el número más grande de la secuancia introducida
print("El número más grande será ", acumuladorNumGrande)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)
