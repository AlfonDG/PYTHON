#Creamos un máximo total de números que el usuario desea introducir
numAIntroducir = int(input("Escriba el número por el que desean dividir: "))

#Crearemos el contador de los divisores a 1 para que pueda dividir entre 1
contadorDivisores = 0

contadorDivisoresTotales = 0

totalMaximo = 200

#Crearemos un bucle que diga que si el número introducido supera a 10 entonces no vuleva a entrar en el bucle, pero de lo contario entrará y mostrará el número que sea divisible por el mismo número
while totalMaximo >= 0:

    contadorDivisores += 1

    #Lo que haremos será decir que si el número que ha introducido el usuario es múltiple del contador
    if numAIntroducir % contadorDivisores == 0:
        contadorDivisoresTotales += 1
        #Finalmente mostraremos el resultado de los números que son divisores
        print("Los divisores entre", numAIntroducir, "es",contadorDivisores,"\n")

    totalMaximo -= 1

print("Los números divisores de", numAIntroducir, "han sido un total de", contadorDivisoresTotales, "números en total")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)