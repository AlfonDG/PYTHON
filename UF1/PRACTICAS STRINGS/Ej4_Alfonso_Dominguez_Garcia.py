#Creamos las variables con lso strings que el usuario introduzca. En este caso serán una para el nombre y las dos para los apellidos
nombre = str(input("Escriba su nombre: "))

apellido1 = str(input("Escriba su primer apellido: "))

apellido2 = str(input("Escriba su segundo apellido: "))

#En este caso creamos una variable que guarde la trasnformación de las variables.
#Solamente usé la función CAPITALIZE para que las tres variables de el nombres + los dos apellidos tengan la primera letera en Mayúsuculas.
#También he concatenado la segunda variable con la tercera que serán los apellidos en uno.
nombrePrimeraMayuscula = nombre.capitalize()

apellidosPrimeraMayuscula = apellido1.capitalize() + " " + apellido2.capitalize()

#Printamos finalmente los dos resultados con las letras mayusculas de cada variable.
print(nombrePrimeraMayuscula + " " + apellidosPrimeraMayuscula)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)