#Crearemos una lista vacía de palabras que el usuario irá rellenando
listaPalabras = []

#Ahora establecemos la variable de parar a "no" por defecto. De esta forma entrará en el bucle WHILE al iniciar
parar = "no"

#Crearemos un bucle que hasta que no se introduzca *si* no parará el bucle
while parar != "si":

    #Le pediremos al usuario que siga introduciendo datos.
    palabrasAnadirLista = str(input("Escriba la palabra que desee: "))

    #En caso de querer parar el bucle debemos de escribir *si* o *no*
    parar = str(input("Desea parar el bucle, diga *si/no*: "))

    #Ahora añadiremos las palabras a la lista.
    listaPalabras.append(palabrasAnadirLista)

#Aquí lo que he hecho ha sido añadir también la última palabra que se ha introducido. Esto lo he realizado así porque al parar el bucle...
#Si se para el bucle sin la última palabra no la contará.
print("")
print(f"Lista -> {listaPalabras}")
#Ahora debemos de crear una variable para que el usuario sustituya el valor de la segunda palabra por la primera
palabraASustituir = str(input("\nEscriba la segunda palabra que desee y esta se sustituirá por la segunda: "))

#Ahora mostraremos la palabra antes de que sustituya.
print(f"Hemos sustituido la palabra *{listaPalabras[1]}*\n")

#Sustituimos la palabra que ha introducido anteriormente por la segunda palabra.
listaPalabras[1] = palabraASustituir

#Finalmente muestro la palabra sustituida y la lista como quedará de forma definitiva.
print(f"Por la siguiente *{palabraASustituir}* y la lista final será *{listaPalabras}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)