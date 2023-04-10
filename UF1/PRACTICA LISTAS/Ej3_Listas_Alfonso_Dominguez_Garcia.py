#Escribimos la lista vacía
lista = []

#Ahora crearemos una variable de tipo INTEGER que permitirá contar cuántas palabras han sido repetidas
vecesPalabrasRepetidas = 0

#Ahora establecemos la variable de parar a "no" por defecto. De esta forma entrará en el bucle WHILE al iniciar
parar = "no"

#Ahora crearemos una variable de tipo STRING vacía que nos permitirá almacenar las palabras repetidas aquí
palabraRepetida = ""

#Crearemos un bucle que hasta que no se introduzca *si* no parará el bucle
while parar != "si":

    #Escribimos la variable de palabra para que el usuario aya introduciendo palabras.
    palabra = str(input("Escriba la palabra: "))

    #Ahora añadiremos a la lista la palabra.
    lista.append(palabra)

    #Usando la función COUNT(palabra) buscará en toda la lista el número de veces que hay repetida una palabra.
    vecesPalabrasRepetidas = lista.count(palabra)

    #Si el número de veces que se repite la palabra es superior a 1 mostrará cál es la palabra repetida en la lista.
    if vecesPalabrasRepetidas > 1:
        palabraRepetida = palabra
    parar = str(input("Desea parar el bucle tiene que decir si/no: "))

#Finalmente mostraremos el resultado.
print(f"{lista} y se ha encontrado que la palabra *{palabraRepetida}* se ha encontrado un total de *{vecesPalabrasRepetidas}* veces repetida")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)