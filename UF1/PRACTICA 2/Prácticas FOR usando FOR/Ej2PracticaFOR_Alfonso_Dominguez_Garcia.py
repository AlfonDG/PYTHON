
#Crearemos la variable que almacenará la suma de todos los números
sumaNumeros = 0

#Crearemos el FOR que permita recorrer los 100 primeros números de 0 a 101 ya que 0 es una posición
for i in range(0,101):

    #Creamos la suma de todos los números que será i a su vez y sumará entre sí los 100 números
    sumaNumeros += i

    #Mostraremos la secuencia de números del 0 al 100
    print(i)

#Finalmente mostramos la suma al completo de todos los números
print("La suma total de todos los números será ", sumaNumeros)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)