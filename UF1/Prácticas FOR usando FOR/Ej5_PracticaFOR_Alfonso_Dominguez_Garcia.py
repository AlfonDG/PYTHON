#Le pedimos al usuario que meta el número máximo de números que desee para parar la secuencia
numMaximoAIntroducir = int(input("Escriba el total de número máximo que desea introducir: "))

#Iniciamos la variable de Contador a 0 
contadorNegativos = 0

#Crearemos el bucle FOR que nos permitirá hacer el rango de entre 0 hasta N que será lo que el usuario escriba
for n in range(0, numMaximoAIntroducir):

    #Escriba aquí los números que quiera ya que hasta n no parará de insertar números
    numAIntroducir = int(input("Escriba aquí los números que desee, cuente que los negativos se los diremos: "))

    #Crearemos el condicional conforme mostrará si hay números por debajo de 0 en este caso han de ser -1 en adelante y de esta forma los contaremos
    if numAIntroducir < 0:
        print(numAIntroducir, "es un número negativo, lo añadiremos al contador\n")
        contadorNegativos += 1

#Finalmente mostramos el contador de todos los números introducidos por el usuario y almacenados.
print("Hay un total de", contadorNegativos, "números negativos introducidos")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)