#Crearemos un total de tres variables. Una será la cade que el usuario quiera escribir y las otras dos serán los carácteres.
#Primera letra que deseé el usuario y luego establecemos el segundo carácter
cadena = str(input("Escriba la cadena/palabra que deseé: "))

caracter1 = str(input("Escriba el primer carácter: "))

caracter2 = str(input("Escriba el segundo carácter: "))

#Ahora crearemos un WHILE que hasta que la longitud de los carácteres sea solamente 1 seguriá introduciendo hasta que cumpla esta condición.
#Es decir que si el usuario escribe más de dos letras pues no podrá continuar con el programa hasta que las introduzca correctamente.
while len(caracter1) and len(caracter2) != 1:

    print("Has introducido más de un carácter. Por favor vuelva a introducir los carácteres de nuevo.\n")

    caracter1 = str(input("Escriba el primer carácter: "))

    caracter2 = str(input("Escriba el segundo carácter: "))

#Ahora crearemos una variable que mediante la función REPLACE reemplazará el carácter1 que será la primer aletra introducida por el usuario por la segunda carcter2.
cadenaReemplazar = cadena.replace(caracter1,caracter2)

#Finalmente mostramos el resultado final con las cadenas que el usuario ha establecido y el resultado obtenido por pantalla.
print(f"La cadena que ha introducido será *{cadena}* y la hemos remplazado por el segundo carácter que será *{caracter2}* y como resultado será *{cadenaReemplazar}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)