#Crearemos dos variables que pediremos al usuario para introducir.
n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo valor: "))

#Creamos la variable suma que es un acumulador de números que se irán añadiendo a esta variable.
suma = 0

#Bucle WHILE que controla que n1 sea más pequeño que n2. Si no es así el bucle no parará
while n1 > n2:
    n1 = int(input("Escriba el primer número: "))
    n2 = int(input("Escriba el segundo valor: "))

#Creamos un bucle FOR que mire el intervalo entre n1 y n2. Contando el número n1 y n2 que será n2 + 1 de esta forma también contará el número de n2 introducido por teclado
#También realizará la suma de todos los valores que hay en el intervalo de números que será la variable n y se sumará a la variable SUMA de esta forma tendremos toda la suma de los números
for n in range(n1,n2 + 1):
    print("El valor intervalo entre n1 y n2 será: ",n,)
    suma += n
print("")
print(f"La suma de los valores será {suma}")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)