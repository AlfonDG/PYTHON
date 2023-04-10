#Primer bucle que va del 0 al 10 de forma normal
for i in range(0, 11):

    #Este mostrará los números sin hacer salto de línea
    print(i, end="    ")

#Aquí, fuera del bucle realizamos el salto de línea
print("\n")

#Segunda secuencia de números en un segundo bucle por separado que mostrará
for x in range(2,21,2):

    print(x, end="    ")

print("\n")

#Tercera secuancia de números que incrementa desde el 20 hasta el número 38 que por eso he añadido 40 por dos posiciones más y de 2 en 2
for n in range(20,40,2):

    print(n, end="    ")

print("\n")

#Cuarta secuancia de números que va del 10 hasta el 30 (en este caso 31 ya que tendremos que añadir una posición) y va incrementando de 4 en 4
for f in range(10,31,4):

    print(f, end="    ")

print("\n")

#Quinta secuancia de números en un quinto bucle que lo que hace es: Del número 40 hasta llegar al 0 (en este caso -1 para añadir una posición más) y decrementa de -5 en -5
for s in range(40, -1, -5):

    print(s,end="    ")

print("\n")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)