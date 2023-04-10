#Primero creamos las variables de cadena y caracter. La variable cadena será la palabra o frase que introduzca el usuario
#Luego escribirá solamente un carácter.
cadena = str(input("Escriba la cadena: "))

caracter = str(input("Escriba el carácter: "))

#Ahora crearemos un condicional que mire la longitud de la cadena para evitar que supere el total de 2 caracteres y que introduzca solamente una letra.
#De esta forma en caso de que lo haga correctamente lo que haremos será comprobar usando la función COUNT contará la cantidad de veces que hay el carácter introducido en la frase
if len(caracter) == 1:

    totalCadena = cadena.count(caracter)

    print(f"Hay un total de *{totalCadena}* de veces que aparece la letra *{caracter}* en la cadena *{cadena}*")
else:
    print("Has establecido más de un carácter. Vuelva a introducir el caracter")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)