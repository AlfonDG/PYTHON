__author__ = "Bilal & Alfonso"
__copyright__="Copyright © 2023 Bilal & Alfonso"

colores = {"rojo": "red", "verde": "green", "negro": "black"}

#crearemos la función de código "error_codigo_diccionario" y pasaremos la lista de "colores" como prámetro
def error_codigo_diccionario(colores):

    #Creamos el try que revisará y comprobará que la variable color escogido es la key de "blanco", es decir añadiremos a esta variable
    #Si la key del diccionario "colores" encuentra el blanco entonces ejecutará el programa si excepciones. De lo contrario lanzará un KeyError.
    try:
        colorEscogido = colores["blanco"]

        #Creamos un bucle FOR con las calves de las keys.
        for claves in colores.keys():

            if colorEscogido in colores[claves]:

                return f"\nEs correcto la variable colorEscogido tiene como valor/value ***{colorEscogido}***, en caso de que solvente el problema con el código"

        #De lo contrario en este "else" lanzamos el KeyError conforme no ha podido encontrar la key de "blanco".
        else:
            raise KeyError

    #En este segundo paso creamos un except KeyError ya que colorEscogido su key no existe en dicho diccionario.
    #Devolveremos con un return la explicación al usuario de tal forma que explique como solventar el problema.
    except KeyError:

        return "\n***Hay un error, estás intentando buscar un clave que no existe o no está añadida en el diccionario, " \
               "\npara solventar este problema tendrás que buscar un color que exista en el diccionario.***"

    #Finalmente printamos que el código se ha ejecutado correctamente, esto es opcional pero, para poder ver que se ha ejecutado el código tanto
    #Si lanza una excepción o como si el código se ejcuta correctamente pintará el finally.
    finally:
        print("Programa ejecutado y finalizado correctamente")

print(error_codigo_diccionario(colores))

print("")

print(__author__)
print(__copyright__)