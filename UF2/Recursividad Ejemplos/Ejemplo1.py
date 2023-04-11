
#RECURSIVIDAD
#1. - Tiene que haber un caso base que haga que la función acabe
#2.- tenemos que definir la función en términos de sí misma (dentro de la función hay una llamada a la propia función.)

#3! = 3 * 2 * 1 = 3 * 2!

#n! = n * (n - 1)! Factorial

#CASOS BASE

n = int(input("Introduzca el valor de N: "))

def factorial_de_n_recursivo(n):

    # CASOS BASE, cuando llega aquí realiza este caso llamado CASO Base y finalmente lo muestra también por pantalla ejecutándolo
    #Es decir, cuando realiza las operaciones y llega a 1 se multiplicará por ejemplo 5 * 4 * 3 * 2 * 1 Factorial y ese 1 será el Caso Base Final
    #Que devolverá el resultado final.

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial_de_n_recursivo(n - 1)

print(factorial_de_n_recursivo(n))