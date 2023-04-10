#Creamos la variable que cuente los números que sean múltiples de 7
contadorMultiples7 = 0

#Creamos el bucle FOR que recorrerá de 0 a 1001 que  serán 1000 ya que el 0 cuenta como posición

for i in range(0,1001):

    #Creamos el conficional que muestra determina que si el números es múltiple de 7 lo añadirá al contador
    if i % 7 == 0:
        print(i, "Sí es múltiplie de 7 se añadirá al contador")
        contadorMultiples7 += 1
        print("")
    #De lo contrario muestra los números que NO sean múltiples de 7 y así mostraremos todos los números de la secuencia
    else:
        print(i, "NO es múltiple de 7")
        print("")

#Mostramos al final la cantidad de números contados que son múltiples de 7
print("Hay un total de", contadorMultiples7, "números múltiples de 7")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)