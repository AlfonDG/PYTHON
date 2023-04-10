altura = int(input("Escriba el número de filas: "))

#Bucle WHILE que controla si el número que ha introducido el usuario es nagtivo. De esta forma si es positivo podrá mostrar la pirámide de asteriscos
while altura <= 0:
    print("Has escrito un número negativo. Vuelva a introducir un número...\n")
    altura = int(input("Vuelva a escribir el número de filas: "))

#Primer FOR que recorrerá el número de filas y printará un espacio en blanco en cada filas haciendo ya los enters para cada asterisco. O saltos de línea
for filas in range(0,altura):
    print("",end="")

    #Segundo bucle FOR que permitirá printar de forma centrada los asteriscos y con sus respectivos espacios en blanco
    #Aquí debemos de al número de altura le restamos las filas que en la segunda iteración será (5 {altura} - 2 - 1) que será 2
    #Por lo tanto deberán de haber un total de 2 espacios en blanco entre el primer asterisco y segundo asteriscos mirando desde la diagonal.
    for espaciosBlanco in range(0,altura - filas - 1):
        print(end="  ")

    #Tercer FOR que printará los asteriscos en cada columna.
    #Lo que hará será empezar de 0 en 1 (La primera vez que itere, es un ejemplo) * 2 -1 que a su vez será 1
    #Y de esta forma mostarremos los números impares de asteriscos.
    for columnas in range(0,filas * 2 - 1):
        print("* ",end="")
    print("")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)