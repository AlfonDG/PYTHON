
#Establecemos las variables Globales aquí de tal forma que podamos, acumular, contar o incluso adivinar los números máximos y mínimos
seguir = True

contadorNumeros = 0

mediaTodosNumeros = 0

numeroMaximo = 0

numeroMinimo = 0

sumaTodosNumeros = 0

#Crearemos un While que mientras sea True no deje de preguntar números al usuario
while seguir == True:

    num = int(input("Escriba los números que desee, se acabará cuando pulse el número 0: "))

    contadorNumeros += 1

    print(contadorNumeros)

    sumaTodosNumeros += num

    print(sumaTodosNumeros)


    #Si el número es 0 parará la secuancia y realizará los cáclulos
    if num == 0:
        print("\nAcabamos la secuencia de números\n")

        mediaTodosNumeros = sumaTodosNumeros / contadorNumeros

        seguir = False

    #Si el número que ha escrito el usuario es menor que cero... Lo añadiremos a la variable de numeroMinimo y habremos encontrado el mínimo en la secuancia de números
    elif num < 0:

        numeroMinimo = num

    #De otro modo si el número es mayor que el resto de todos los números encontrados pues lo guardaremos en la variable numeroMaximo y sabremos el Numero Máximo de nuestra secuencia
    elif num > contadorNumeros:

        numeroMaximo = num

    #Si el usuario no establece el número 0 que siga la secuencia!!!

    else:
        seguir = True

print("El total de número introducidos han sido", contadorNumeros, "\nLa suma de todos los números ha sido",sumaTodosNumeros, "\nEl número máximo encontrado será", numeroMaximo , "\nEl número mínimo encontrado ha sido", numeroMinimo ,"\nY la media aritmética de todos los números será", float(mediaTodosNumeros))

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)