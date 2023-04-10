#Crearemos dos variables que pediremos al usuario para introducir.
n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo valor: "))

suma = 0
#Bucle WHILE que controlará que mientras que n1 sea mayor que n2 seguirá pidiendo números. Ya que queremos que n1 sea más pequeño que n2
while n1 > n2:
    n1 = int(input("Vuelva a escribir el primer número: "))
    n2 = int(input("Vuelva a escribir el segundo valor: "))

#Creamos un bucle FOR que mire el intervalo entre n1 y n2. Contando el número n1 y n2 que será n2 + 1 de esta forma también contará el número de n2 introducido por teclado
for n in range(n1,n2 + 1):
    print(f"El intervalo de los valores será {n}")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)