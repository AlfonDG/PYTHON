__author__ = "Alfonso"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

#Num de veces que ejecutará el usuario las funciones y sub_funciones.
numVeces = int(input("Introduzca el número de veces que desea llamar a las funciones y sub_funciones: "))

#Ahora crearemos la función "crear_funcio_comptador" que tendrá como parámetro el valor de n introducido antriormente por el usuario.
def crear_funcio_comptador(n):

    #Ahora crearemos una sub función que se llamará comptar_fins_n la cual permitirá desde una sub función tener un bucle FOR
    #Que recorrerá desde 1 hasta n + 1 de tal forma que irá sumando n hasta llegar al número esatblecido por el usuario.
    #Finalmente printamos el valor de i dentro de la función de tal forma que mostrará los valores hasta N que haya establecido el usuario
    def comptar_fins_n():

        for i in range(1, n + 1):

            print(i)
    #Ahora llamamos a la sub_función que permitia realizar esta operación.
    comptar_fins_n()


#Aquí crearemos un bucle WHILE que nos permitirá llamar a las funciones el número de veces que el usuario quiera.
while numVeces > 0:

    # En este apartado le pediremos al usuario un valor con tal de que este valor sea un límite de número máximos a contar.
    # Es decir, si el usuario introduce por ejemplo 5... Contará desde 1 hasta el valor de 5.
    n = int(input("\nHasta que número de N veces desea contar?: "))

    #Aquí llamamos a la función principal que tendrá como parámetro N
    crear_funcio_comptador(n)

    #Decrementamos la variable de numVeces a -1 hasta que llega a 0 y paramos el bucle.
    numVeces -= 1

print("")
print(__author__)
print(__copyright__)

