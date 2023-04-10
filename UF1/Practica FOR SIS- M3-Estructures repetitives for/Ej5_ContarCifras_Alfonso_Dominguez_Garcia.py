numeroEntero = int(input("Escriba el número entero: "))

#Bucle WHILE que controlará si el usuario inserta un número negativo
while numeroEntero < 0:
    print("Lo sentimos, pero has establecido un valor menor a 0 o negativo en la secuencia de números.\n")
    numeroEntero = int(input("Vuelva a escribir el número entero: "))

pasarNumeroString = str(numeroEntero)

contadorCifras = 0

#Mostraremos la secuancia que el usuario ha escrito por pantalla para que tenga una idea de su secuencia y como la he desglosado.
print("Ha escrito la secuencia de números", pasarNumeroString,"devolveremos la cantidad de cifras")

#Creamos un bucle FOR que pasará la cadena con la secuancia de números e iremos contando cúantas cifras tiene final
for i in pasarNumeroString:

    print("La cifra es: ",i)

    contadorCifras += 1

print("Hay un total de", contadorCifras,"cifras que hemos podido contar")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)