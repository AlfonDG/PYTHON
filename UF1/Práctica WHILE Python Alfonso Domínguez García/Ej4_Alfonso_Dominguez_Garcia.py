clave = "eureka"

numIntentos = 3

#Bucle que cuente si el número de intentos es inferior a 0 el bucle seguirá
while numIntentos > 0:

    #Pedimos al usuario el nombre de la clave
    intentoClave = str(input("Escriba la clave que crea que es: "))

    #Restamos el número de intentos
    numIntentos -= 1

   #Condicionales para intento de adivinar la clave
    if intentoClave == clave:

        print("Enhorabuena, has adivinado la clave que era", clave)

        print("Has adivinado la clave cuando el número de intentos ha sido", numIntentos, "intentos")

        numIntentos -= 3

        #break

        '''Podemos intentar usar un Break para frenar el bucle una vez hemos adivinado la clave o bien podemos restar
         todos los intentos para que no vuelva a entrar al bucle de nuevo'''

    else:

        print("No has adivinado la clave, tienes un total de", numIntentos, "intentos")


print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)