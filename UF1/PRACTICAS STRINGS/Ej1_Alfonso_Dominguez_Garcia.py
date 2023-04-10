#Primero creamos la variable cadena y subcadena que una será la palabra o frase que quiera el usuario.
#Y la segunda será la subcadena que deseé para comprobar que la palabra empieza por la primera palabra de la primera cadena
cadena = str(input("Escriba la cadena que desee: "))

subcadena = str(input("Escriba la subcadena: "))

#Creamos otra variable que permita ver si empieza o no por la primera letra o letras de la frase o cadena.
empiezaCadenaSubcadena = cadena.startswith(subcadena)

#Mostraré el resultado final diciendo el valor que el usuario ha introducido da True en caso de que empieze por las letras de la cadena.
#De lo contarrio mostrará False.
print(f"La cadena introducia es *{cadena}*, la subcadena será *{subcadena}*. Da un valor de *{empiezaCadenaSubcadena}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)