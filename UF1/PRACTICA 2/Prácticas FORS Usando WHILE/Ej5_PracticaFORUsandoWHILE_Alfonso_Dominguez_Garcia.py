#Crearemos un contador de Números que sean negativos

contadorNegativos = 0

numMaximos = int(input("Escriba el límite de los números máximos: "))

#Crearemos un bucle WHILE que indique que si el número máximo del usuario sea menor que 0 siga entrando en el bucle para seguir introduciendo números
while numMaximos > 0:

    #Aquí tendremos que restar la cantidad de numMaximos hasta llegar a 0 o inferior, de esta forma
    numMaximos -= 1

    numAIntroducir = int(input("Escriba los números que quiera. El número negativo se añadirá a contador: "))

    if numAIntroducir < 0:

        #Mostraremos al usuario que en caso de que sea el número negativo se lo indicaremos al usuario y que lo añadiremos a contador de números negativos
        print(numAIntroducir, "es un número negativo, se añadirá al contador")

        #Añadiremos a contadro de negativos 1 para contar cuántos números hay que son negativos
        contadorNegativos += 1

#Finalmente mostramos la cantidad de números que son negativos
print("Hay un total de", contadorNegativos,"números que son negativos")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)