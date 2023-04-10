__author__ = "Bilal & Alfonso"
__copyright__="Copyright © 2023 Bilal & Alfonso"

#Creamos la función llamada "error_bloque_codigo"
def error_bloque_codigo():

    #Primero creamos un try de tal forma que tendrá una variable "resultado" que intenará sumar 15 + una string que es 20 en este caso.
    #Saltará un mensaje de TypeError
    try:
        #En este caso realizará la suma errónea de 15 + la string de 20. En caso de que se resuelva el código de forma correcta devolvverá el return
        #Pero si no es el caso lanzará la exception TypeError.

        resultado = 15 + "20"

        #Mensaje conforme el código es correcto si se arregla el error de la string.
        return "***El código es correcto, en caso de que se solventara el problema.***\n"

    #En caso de que la primera parte de código no se haya cumplido lanzará el mensaje de except TypeError y le devolveremos un return
    #Conforme el mensaje servirá como ayuda al usuario a poder reparar el error.
    except TypeError:

        return "***Error, estás intentando sumar un número con una string, para solventar este problema tendrás que quitar las strings del número." \
               "\nPara solventar este problema deberíamos de modificar la string de 20 y pasarla a int(20) y de esta forma quedaría resuelto.***"

    #Finalmente printamos que el código se ha ejecutado correctamente, esto es opcional pero, para poder ver que se ha ejecutado el código tanto
    #Si lanza una excepción o como si el código se ejcuta correctamente pintará el finally.
    finally:
        print("Programa ejecutado y finalizado correctamente\n")

print(error_bloque_codigo())

print("")

print(__author__)
print(__copyright__)