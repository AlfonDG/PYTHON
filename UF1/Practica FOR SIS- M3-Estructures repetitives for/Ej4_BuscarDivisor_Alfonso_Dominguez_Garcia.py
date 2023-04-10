numEntero = int(input("Escriba aquí el número entero positivo: "))

#Creaemos un bucle WHILE que haga de numEntero se ainferior a 1 tendrá que volver a escribir un número de nuevo.
while numEntero < 1:
    print("Has escrito un valor inferior a 1, 0 o negativo... Vuelva a intentarlo por favor.")
    numEntero = int(input("Escriba de nuevo el número entero positivo: "))

#Aquí inicializaremos las varibles de SEMÁFOROS iniciadas a 0 e irán contando cuantos divisores se encuentran en Rojo (no es divisor del número N), Verde (es divisor de número N)
semaforoVerde = 0

semaforoAmbar = 0

semaforoRojo = 0

#Crearemos un bucle FOR que haga de 1 hasta numEntero + 1 que será desde 1 mostrará si son divisores.
for d in range(1,numEntero + 1):

    #Aquí debemos de establecer las variables de CONTROL de tipo semáforo. Lo que hay que mirar realizando un total de 3 condicionales es si el númeroe s divisor entre N
    #En caso de que SÍ lo sea lo añadiremos a semaforoVerde, si no es lo añadiré al semáforoRojo y si no encuentra divisores entre el número N y d lo añadiremos al Ambar.
    if numEntero % d == 0:
        print(f"{d} SÍ es divisor de {numEntero}, se añadirá al contador de Semáforo en VERDE")
        semaforoVerde += 1
    elif numEntero % d != 0:
        print(f"{d} NO es divisible entre {numEntero} se añadirá al semáforo ROJO")
        semaforoRojo += 1
    else:
        print(f"No se ha encontrado ningún divisor. Se añadirá a la variable de semáforo ÁMBAR\n")
        semaforoAmbar += 1
print(f"\nHay un total de {semaforoVerde} divisores entre {numEntero}\nHay un total de {semaforoRojo} que no han sido divisores de {numEntero}\nHay un total de {semaforoAmbar} que no se han encotrado divisores entre {numEntero}")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)