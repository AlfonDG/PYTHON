#Creamos la lista de palabras vacía.
listaPalabras = []

#Creamos la variable de parada para el bucle. En caso de que se escriba que *si* dejaremos de entrar en el bucle
parar = "no"

#Crearemos un bucle WHILE que hasta que no se introduzca *si* no parará el bucle
while parar != "si":

    #Le pedimos al usuario las palabras que sean necesarias
    palabrasAnadirLista = str(input("Escriba la palabra que desee: "))

    #Lo siguiente que haremos será añadir a la lista de palabras las palabras introducidas por el usuario
    listaPalabras.append(palabrasAnadirLista)

    #Ahora le preguntaremos al usuario si desea continuar con el bucle escribiendo *si/no*
    parar = str(input("Desea parar el bucle, diga *si/no*: "))

#Ahora le pedimos al usuario que introduzca una palabra que desea eliminar.
palabraAEliminar = str(input("\nIntroduzca la palabra que desea eliminar de la lista: "))

#Mostramos al usuario la palabra que vamos a eliminar de la lista.
print(f"Procedemos a eliminar la palabra *{palabraAEliminar}* de la lista...")

#Ahora eliminamos la palabra de la lista y de esta forma mostraremos a continuación el resultado.
listaPalabras.remove(palabraAEliminar)

#Mostramos la lista de palabras y conforme se ha elimiando una palabra de la lista.
print(f"Finalmente la lista quedará de la siguiente forma -> *{listaPalabras}*")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)