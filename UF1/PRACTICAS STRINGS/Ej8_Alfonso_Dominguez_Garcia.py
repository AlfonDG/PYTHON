#Crearé la varibale que el usuario deseé
cadena = str(input("Escriba la palabra/frase que deseé: "))

#Crearemos una varibale que permita invertir la cadena
cadenaReverse = cadena[::-1]

#Ahora crearemos un condicional que permita mirar si la cadena que ha introducido el usuario es igual que la cadena pero INVERTIDA.
#Tras comprobar que es así mostraremos el resultado diciendo a la persona si es o no palíndroma la palabra introducida.
if cadena == cadenaReverse:
    print(f"La cadena *{cadena}* es palíndroma ya que se escribe igual normal que invertida. Invertida sería *{cadenaReverse}*")
else:
    print(f"No es una palabra palíndroma, ya que *{cadena}* no es palíndroma. Invertida sería *{cadenaReverse}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)