#Crearemos dos variables que pediremos al usuario para introducir.
n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo valor: "))

#Bucle WHILE que controla que n1 sea más pequeño que n2. Si no es así el bucle no parará
while n1 > n2:
    n1 = int(input("Escriba el primer número: "))
    n2 = int(input("Escriba el segundo valor: "))

#Crearemos un bucle FOR que recorrerá el intervalo entre n1 y n2 que mostrará los valores de forma DECRECIENTE, es decir de n2 hasta n1 con PASO -2
#De esta forma irá restando las cantidades de -2 en -2 y solamente mostrará los PARES sin necesidad de un IF. Si quisieramos los imapres sería ir de -3 en -3 o bien sumar un +1 en n2
for pares in range(n2,n1,-2):
        print("El número par entre n1 y n2 es: ",pares)
print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)