num = int(input("Escriba el número de filas: "))

#Buvle While que controlará si el valor que ha introducido el usuario es negativo. De esta forma podrá printar la pirámide de letras
while num < 0:
    print("Has escrito un número negativo. Vuelva a introducir un número...\n")

    num = int(input("Vuelva a escribir el número de filas: "))

#Primer FOR que recorrerá el número de filas
for i in range(0,num + 1):
    #Segundo FOR que printará el número de A para formar la piramide
    for x in range(0,i):
        print("a",end="")
    print("")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)