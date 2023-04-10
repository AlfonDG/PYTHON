n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo valor: "))

suma = 0

#Crearemos una bucle WHILE que permita saber si el número n1 es más grande
while n1 > n2:
    n1 = int(input("Vuelva a escribir el primer número: "))
    n2 = int(input("Vuelva a escribir el segundo valor: "))

#Crearemos una variable FOR que permite hacer un intervalo entre n1 y n2
for n in range(n1,n2 + 1):

    #El siguiente paso será crear un condicional que haga que la variable n contador revise si el número es múltiple de n1 y se contará
    if n % n1 == 0 and n <= n2:
        print("Los múltiples más grandes de N1 y más pequeños o iguales a N2 es ->",n)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)