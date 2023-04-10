#Crearemos la lista de carácteres vacía
listaCaracteres = []

#Le pedimos al usuario una cadena por teclado
cadena = str(input("Escriba la cadena por teclado: "))

#Ahora crearemos la segunda lista donde almacenaremos la cadena establecida sin espacios
segundaListaSinEspacios = []

#He definido también
cadenaSinEspacios = ""

#Crearé un bucle FOR que permita recorrer todos los carácteres uno por uno y añadirlos a una lista.
for i in cadena:

    #Añadiremos I con los carácteres uno por uno por ejemplo de la cadena *alfonso*
    #Añadirá a la lista "a","l","f","o","n","s","o" y lo que queremos es que la cadena otra vez se unifique.
    listaCaracteres.append(i)

    #Para poder unificar la cadena usaré la función JOIN de tal forma que unirá cada carácter de la cadena para completar la cadena.
    cadenaSinEspacios += i.join(i)

#Ahora y finalmente añadiremos la cadena sin espacios a la segunda lista y ya tendremos unificado.
segundaListaSinEspacios.append(cadenaSinEspacios)

#Primero printamos la lista con los valores de la cadena sin unificar.
print(f"Lista de carácteres uno por uno -> *{listaCaracteres}*\n")

#Finalmente printamos la lista de los valores de la cadena unificados.
print(f"Lista de carácteres unificado gracias a la función JOIN -> *{segundaListaSinEspacios}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)