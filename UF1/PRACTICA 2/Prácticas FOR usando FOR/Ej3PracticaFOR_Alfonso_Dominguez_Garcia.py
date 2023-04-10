#Primero le pediremos al usuario que nos escriba e introduzca el límite que usaremos para

numMaximoIntroducido = int(input("Escriba el máximo de números que desea mostrar: "))

#Ahora crearemos la variable que mostrará
numeroMasGrande = 0

for i in range(0, numMaximoIntroducido):

    numAIntroducir = int(input("Escriba aquí su número: "))

    #Si el número que introduzca el usuario supera a un número que esté dentro de la secuencia (en este caso i que mostrará los N números que vaya metiendo el usuario) será el más grande encontrado
    if numAIntroducir > i:

        #Almacenaremos ese número en la variable
        numeroMasGrande = numAIntroducir

#Finalmente lo mostramos por pantalla el resultado del número más grande
print("El número más grande que hemos encontrado ha sido", numeroMasGrande)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)