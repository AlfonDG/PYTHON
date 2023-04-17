#Primero creamos la variable pasos que pedirá al usuario el valor máximo de números que desea repetir la secuancia.

pasos = int(input("Introduzca el valor de num y te daremos la secuencia correcta de valores: "))

#Ahora definiremos la función "secuencia_numeros" y le pasamos los argumentos "num" (variable estática) y "pasos" que será la variable anterior

def secuencia_numeros(num,pasos):

    #En este condicional if le pediremos al usuario que cuando los pasos sea igual a 0 devolverá 1 la función.
    #De esta forma si el usuario escribe que los pasos sean 0 pues no devolverá nada. Pero si los pasos == 1
    #Devolverá el valor de 1.

    if pasos == 0:

        return 1

    #Luego en el condicional else. Podemos ver que realizará un print de num * num que será 1 * 1.
    #Y la función recursiva lo que hará será la primera pasada será 1 * 10 = 10 + 1 = 11 y restaremos de los pasos - 1 con tal de que decremente la función
    #La segunda iteración será print(11 * 11) = 121 y luego realizará 121 * 10 + 1 = 1211
    else:

        print(num*num)

        return secuencia_numeros(num * 10 + 1,pasos - 1)

secuencia_numeros(1,pasos)

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)