#Creamos la primera varibale para que l usuario pueda introducir la cadena o frase que deseé.
cadena = str(input("Escriba la palabra/frase que deseé y yo la convertiré en mayúsculas o minúsculas: "))

#Craremos una variable que almacene el resultado de la cadena transformada en Mayúsculas o Minúsuclas según introduzca el usuario.
#He usado la función SWAPCASE que permite trasnformar la cadena que haya en Minúsuculas a Mayúsculas y viceversa.
cadenaMayusculasMinusculas = cadena.swapcase()

#Printamos el resultado de la cadena introducida y el resultado de la variable a transformar Mayúsculas y Minúsuculas.
print(f"Usted introdujo la cadena *{cadena}* y le devuelvo la cadena a mayúsuclas o minúsuclas *{cadenaMayusculasMinusculas}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)