#Para realizar la función de desglose de billetes primero debemos de pedir un valor dinámico al usuario
valorPago = int(input("Introduzca un valor en billetes y nosotros lo desglosaremos: "))

#En este caso crearemos la función desglose de billetes.
def desglossamentBillets(valorPago):

    #Definimos dentro de la función la tupla con los billetes y la tupla con las monedas respectivamente.
    tuplaBilletes = (500, 200, 100, 50, 20, 10, 5)

    tuplaMonedas = (2, 1)

    #Aquí he añadido un extra que será un diccionario que cada key serán (billetes) o (monedas) y los valores será el resultado de la divisón de los valores.
    diccionarioValoresDesglose = {}

    #Realizamos un bucle FOR que recorrerá los billetes.
    for b in tuplaBilletes:

        #Ahora añadiremos al diccionario el valor de la división. Sustituyendo los valores sería igual a ->
        #diccionarioValoresDesglose[500] = 434 // 500 | La key de diccionario será b cada vez. Es decir 500,200,100 etc...
        diccionarioValoresDesglose[b] = valorPago // b

        #Y ahora para obtener el resultado del residuo debemos de al valor restarle la cantidad de lo siguiente:
        #434 -= diccionarioValoresDesglose[500] * 0 de esta forma tendremos el módulo de forma manual en la operación.
        valorPago -= diccionarioValoresDesglose[b] * b

    #Ahora realizamos el bucle FOR que recorrerá las tuplas de monedas.
    for m in tuplaMonedas:

        #Realizamos exactamente la misma operación realizada con los billetes tanto para extraer y restar el residuo cada vez.

        #Guardaremos en el diccionario como valores el valor de la divisón. Y finalmente realizamos la operación de residuo.
        diccionarioValoresDesglose[m] = valorPago // m

        valorPago -= diccionarioValoresDesglose[m] * m

    #Finalmente mostramos las claves y valores del diccionario haciendo un .items y mostramos los resultados de las divisiones que serán los valores
    #Y mostraremos también las claves que serán los billetes tanto de billetes como las monedas de 2 y de 1 euros.
    for claves,valores in diccionarioValoresDesglose.items():

        #Aquí comprobamos que si las claves se encuentran en la lista de tuplas tanto de monedas o billetes cambiaremso el print
        #De esta forma lo haremos más elegante a la hora de printar y sin errores.

        if claves in tuplaBilletes:
            print(f"\nHay un total de **{valores}** billetes de ***{claves}*** euros.")

        elif claves in tuplaMonedas:
            print(f"\nHay un total de **{valores}** monedas de ***{claves}*** euros.")

#Llamamos a la función sin realizar un print ya que el resultado devolverá NONE ya que no hemos especificado un return.
desglossamentBillets(valorPago)

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Rayan Haizour"

print(autor)
print(copy)