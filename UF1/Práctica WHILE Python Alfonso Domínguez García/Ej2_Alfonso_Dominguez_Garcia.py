seguir = True

mediaAritmetica = 0

contadorNumeros = 0

sumaNumeros = 0

while seguir == True:

    numero = int(input("Escriba un número por teclado: "))

    if numero <= -2:
        print("No puedes establecer valores que sean inferiores a -1")

        seguir = True

    elif numero == -1:
        print("Acabamos la secuencia de números, procedemos a calcular la media aritmética")

        print("")

        print("Hay un total equivalente a", contadorNumeros, "números almacenados")

        mediaAritmetica = sumaNumeros / contadorNumeros

        seguir = False

       #Este else está creado para evitar que cuente un número cuando el usuario establezca el valor -1 y de esta forma tendremos la media bien hecha
    else:
        contadorNumeros += 1

        sumaNumeros += numero

        print(sumaNumeros)

        seguir = True

print("La media aritmética total de los números será", mediaAritmetica )

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)