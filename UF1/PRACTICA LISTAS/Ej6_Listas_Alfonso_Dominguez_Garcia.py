#Crearemos la dos listas vacías.
lista1 = []

lista2 = []

#Variable d einicio que permitirá iniciar en el bucle WHILE.
parar = "no"

#Bucle WHILE que permitirá entrar si la opción de parar bucle sea NO continuará de lo contarrio parará.
while parar != "si":

    #Creamos la variable para pedirle una palabra al usuario.
    escribirPalabra1 = str(input("Escriba una palabra: "))

    #Ahora añadimos la palabra a la lista1.
    lista1.append(escribirPalabra1)

    #Le pedimos al usuario una sagunda palabra que esta se añadirá a la lista2
    escribirPalabra2 = str(input("Escriba la segunda palabra: "))

    #Y añadiremos a la lista2 la segunda palabra.
    lista2.append(escribirPalabra2)

    #Y ahora le pediremos al usuario si desea parar el bucle.
    parar = str(input("\nDesea parar el bucle *si/no*: "))

    #En caso de que escriba el usuario que sí. Procederemos a crear un bucle FOR.
    if parar == "si":
        #Este bucle FOR nos permitirá recorrer todos los elementos de la lista1 y lo que haremos será comparar los indices.
        #En caso de estar repitiendo un valor en la misma lista1 lo eliminaremos
        for i in lista1:
            if i == i:
                print("Hemos encontrado un valor repetido en lista2 y procedemos a eliminarlo de la lista1")
                lista1.remove(i)
    #De lo contrario seguirá el usuario con el bucle y pedirá palabras.
    else:
        print("Continuaremos con el bucle")

#Mostraremos los resultados de ambas listas y veremos que los nombres de la primera se eliminarán los nombres y en la segunda se quedarán.
print(f"La lista número 1 será -> {lista1}\n")
print(f"La lista número 2 será -> {lista2}")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)