#Creamos una variable que permita al usuario escribir una frase o cadena que quiera.
cadena = str(input("Escriba la frase/palabra que deseé y yo la invertiré: "))

#Crearé una segund avariable que permita revertir la cadena que el usuario ha introducido
cadenaReverse = cadena[::-1]

#Finalmente le mostraré por pantalla al usuario el resultado de la cadena invertida.
print(f"Usted introdujo la cadena *{cadena}* y yo la he invertido de la siguiente forma -> *{cadenaReverse}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)