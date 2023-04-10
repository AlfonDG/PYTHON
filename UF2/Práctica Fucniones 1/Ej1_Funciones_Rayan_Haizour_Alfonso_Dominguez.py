#Aquí debemos de definir una variable para que el usuario introduzca una frase o palabra
paraula = input("Introdueix una paraula: ")

#Ahora definiremos la función y esta función comprobará si es Alfabética
def leerPalabraAlfabetica(paraula):

    #Primero establecemos una variable de control que estará en True
    ordalfabetic = True

    #Este bucle FOR recorrerá la palabra introducida hasta -1 sin contar la útima letra
    #De esta forma comprobamos que las dos letras centrales sean de forma ordenada que las dos últimas. Si esto se cuemple sabremos que no está ordenado
    #Por eso se establece que ordalfabetic es False en este caso ya que no está en orden alfabético
    for i in range(len(paraula)-1):
        if paraula[i] > paraula[i+1]:
            ordalfabetic = False
            break

    #Finalmente si la variable ordalfabetic es True sabremos que la palabra es alfabética de lo contrario no será una palabra alfabética.
    if ordalfabetic == True:
        print("La paraula", paraula, "és alfabètica.")

    else:
        print("La paraula", paraula, "no és alfabètica.")

#Llamamos a la función de la siguiente forma sin realizar print ya que devolverá None en caso de que no haya un return
leerPalabraAlfabetica(paraula)

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)