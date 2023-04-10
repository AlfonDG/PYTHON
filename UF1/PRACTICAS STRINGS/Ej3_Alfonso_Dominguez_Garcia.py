#Creamos la primera variable que escribirá el usuario a introducir
cadena = str(input("Escriba la cadena/frase que desee: "))

#Crearemos una variable que permita contar el número de palabras separadas por espacios que hay en una string.
#En este caso la función SPLIT partirá y seprará las palabras en cadenas y si hacemos la len o longitud de la cadena.
#Tendremos contadas las palabras que el usuario escribirá por pantalla
contadorPalabras = len(cadena.split())

#Finalmente mostraré el resultado de la cadena que ha introducido el usuario, el número de palabras que hay en la cadena.
#Y finalmente le mostraré la cadena pero partida con SPLIT para saber como separará las palabras.
print(f"Usted ha introducido la frase *{cadena}*. Hay un total de *{contadorPalabras}* palabras que serán *{cadena.split()}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)