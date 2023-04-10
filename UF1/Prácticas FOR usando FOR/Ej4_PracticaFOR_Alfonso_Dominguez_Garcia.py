
numIntroducido = int(input("Escriba un número y le mostraré sus divisores: "))

contadorDivisores = 0

#En este caso en este bucle FOR cabe destacar que no podemos empezar por 0 ya que no podemos dividir entre 0 sinó que ha de ser 1
#Sumamos a la variable 1 ya que la posición que ha perdido la volvemos a añadir... Por loq ue no habremos perdido las posiciones para mostrar los divisores del números

for x in range(1,numIntroducido + 1):

    #Crearemos un condicional que nos diga si el número que ha metido por teclado el usuario es divisible por x que será 1,2,3,4 hasta Número pues se lo haremos saber al usuario mostrándolo por pantalla
    if numIntroducido % x == 0:

        #Añadiremos al contador de números + 1 y de esta forma contaremos los divisores que tenga en total el número que haya introducido el usuario
        contadorDivisores += 1

        #Aquí mostraremos los números que sean divisibles por el número que quiera el usuario. En este caso no ha sabido como almacenar esto en una variable con tal de poder mostrarlos todos.
        print(x, "será divisor de", numIntroducido)

print("Los números divisores de", numIntroducido, "han sido un total de", contadorDivisores, "números en total")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)