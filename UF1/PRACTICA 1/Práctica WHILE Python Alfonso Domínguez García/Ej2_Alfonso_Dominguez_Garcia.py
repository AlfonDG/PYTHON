seguir = True

medianaAritmetica = 0

contadorNumeros = 0

sumaNumeros = 0

while seguir == True:

    numero = int(input("Escriba un número por teclado: "))

    contadorNumeros += 1

    if numero <= -2:
        print("No puedes establecer valores que sean inferiores a -1")

        seguir = True

    elif numero == -1:
        print("Acabamos la secuencia de números, procedemos a calcular la media aritmética")

        print("")

        print("Hay un total equivalente a", contadorNumeros, "almacenados")

        sumaNumeros = sumaNumeros + contadorNumeros

        medianaAritmetica = sumaNumeros / contadorNumeros

        seguir = False

print("La media aritmética total de los números será", medianaAritmetica )

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)