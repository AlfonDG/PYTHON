import random

print('''\nBenvingut a Botswana! 

Has robat un elefant per salvar-lo de les cruels matances, per aconseguir-ho has de 
travessar 200 km el desert del Kalahari.

Els caçadors furtius volen recuperar el seu elefant i surten en persecució teva! hauràs 
de sobreviure al desert i córrer més que els caçadors bosquimanos.

[Llegenda Prints Equivalents al Joc] -> ^ Advertencia o Avis
                                        * Recompensa o Has Guanyat
                                        ! Fallida o Has perdut''')

#Creamos las variables iniciales a 0, excepto la distancia recorrida por los bosquiamanos que será de -20
#Y los glops de la cantimplora que será un random.random de 5 hasta 9 en este caso 4 y 10 NO son incluidos, ya que usando RANDOM.RANDOM no se incluyen y dará un número decimal
#Lo que he hecho ha sido pasar esta variable a INT y de esta forma redondeará el número siempre hacia abajo de los decimales. Por lo que nunca dará el número 4 y 10 (NO estarán incluidos) sino 5 y 9 (Estarán incluidos).

kilometresRecorreguts = 0

set = 0

cansamentElefant = 0

distanciaRecorregudaCacadors = -20

glopsCantimplora = int(random.random() * 5) + 5

contadorGlopsAiguaFets = 0

trobarOasi = random.randrange(0,20)

continuarBucle = True

while continuarBucle == True:

    #A partir de aquí es el menú principal y el inicio del juego.
    print('''
    A. Beure de la cantimplora.
    B. Velocitat moderada cap endavant.
    C. A tota velocitat cap endavant.
    D. Para i descansa.
    E. Comprova el teu estat. 
    Q. Sortir.\n''')

    opcion = str(input("Què tries?".center(18)))
    
    #Comprobará que la variable opción. No importará si el usuario escribe en Mayúscula o Minúscula.
    #Ya que he verificado que tanto si escribe por ejemplo "A" como "a" lo escribirá en mayúsculas revisará automáticamente
    #Si el usuario ha escrito en minúsculas lo transformará automáticamente en mayúsculas.
    opcion = opcion.upper()

    #Vienen los condicionales que mostrarán las opciones que el usuario quiera.
    if opcion == "A":

        #He comprobado que si al usuario le quedan menos de 1 glop en la cantimplora antes de llegar a 0 saltará el error pero seguimos el juego.
        #No resetearemos la sed del elefante.
        if glopsCantimplora <= 1:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("No queden glops a la cantimplora!")
            print("Error, seguim amb el joc però no podrà beure aigua.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continuarBucle = True

        #De lo contrario restamos un galop a la cantimplora, reseteamos la sed del elefante a 0
        #Seguimos con el juego.
        else:
            glopsCantimplora -= 1
            print("\n------------------------------------------")
            print(f"Queden un total de {glopsCantimplora:.0f} glops a la cantimplora")
            contadorGlopsAiguaFets += 1
            set = 0
            continuarBucle = True
            print("------------------------------------------")

    #Si escogemos la opción B o b el elefante avanzará una velocidad moderada de kilòmetres entre 5 y 12. Usuaré randitn para incluir los dos números.
    #Recorremos la distancia y subimos + 1 a la sed del elefante y +1 a su cansancio. También moveremos a los Cazadores entre 8 y 13 hemos incluido los dos usando el randint.
    #Pero he preferido solamente establecer el rango de 8 a 13 no de 7 a 14 que ninguno de los dos estarán incluidos.
    elif opcion == "B":
        print("\n------------------------------------------")
        print(f"Velocitat moderada cap endavant")
        kilometresRecorreguts += random.randint(5,12)
        print(f"Has recorregut un total de {kilometresRecorreguts} kilòmetres")
        print("------------------------------------------")
        set += 1
        cansamentElefant += 1
        distanciaRecorregudaCacadors += random.randint(8,13)
        continuarBucle = True

    #Ahora avanzamos según la opción C o c a toda velocidad que será un número aleatorio entre 10 y 20 incluidos.
    #Sumaremos + 1 a la sed del elefante. Su cansancio avanzará un número entre 2 y 2 incluidos en vez de usar 1 y 3 que no están ambos incluidos.
    elif opcion == "C":
        print("\n------------------------------------------")
        print("A tota velocitat cap endevant!!!")
        kilometresRecorreguts += random.randint(10,20)
        print(f"Has recorregut un total de {kilometresRecorreguts} kilòmetres recorreguts")
        print("------------------------------------------")
        set += 1
        cansamentElefant += random.randint(2,2)
        distanciaRecorregudaCacadors += random.randint(8,13)
        continuarBucle = True

    #Si el usuario decide marcar la letra D o d lo que hará será descansar y reiniciar el cansancio del elefante a 0 pero moverá a los cazadores
    #Un random entre 7 y 14 pero como estos dos no estaban incluidos lo que he hecho ha sido usar un RANDOM.RANDINT que permitirá incluir el 8 hasta el 13 incluidos.
    elif opcion == "D":
        print("\n------------------------------------------")
        print(f"Has decidit parar per descansar")
        cansamentElefant = 0
        print("------------------------------------------")
        print(f"L'Elefant t'ho agraeix aquest descans")
        distanciaRecorregudaCacadors += random.randint(8,13)
        print("Pero els caçadors s'han apropat... Tingues cura...")
        print("------------------------------------------")

    #La opción E o e nos permitirá mostrar un pequeño submenú que mostrará el estado actual del juegador y de como está el elefante. Distancia recorrida en kilómetros.
    #El número de veces que ha bebido de la Cantimplora, los tragos que te quedan en la cantimplora y finalmente a cuántos kiómetros están los cazadores.
    elif opcion == "E":
        print("\n------------------------------------------")
        print(f"Kilòmetres Recorreguts = {kilometresRecorreguts}")
        print(f"Vegades que has begut de la cantimplora = {contadorGlopsAiguaFets:.0f}")
        print(f"Glops que et queden = {glopsCantimplora:.0f}")
        print(f"Els bosquimanos són a {kilometresRecorreguts - distanciaRecorregudaCacadors} kilòmetres darrere teu")
        print("------------------------------------------")

    #Con la opción Q o q saldremos del juego en caso de que queramos salir.
    elif opcion == "Q":
        print("\n-------------------------------------------------------------")
        print("Sortint del joc.... Gràcies per jugar a Botswana Elephant.")
        print("---------------------------------------------------------------")
        continuarBucle = False

    #De lo contrario no habremos escrito una opción válida y volverá al menú principal del juego para volver a escribir.
    else:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("No has sel·leccionat una opció adecuada. Torna a provar")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        continuarBucle = True

    #Lo que haré será crear distintos condicionales que uno permitirá saber si los cazadores están cerca... Si el usuario ha encontrado un Oasis por suerte.
    #También mensajes de alerta conforme el elefante está cansado o bien no le quedan tragos en la cantimplora etc...
    if kilometresRecorreguts >= 200:
        print("\n***********************************")
        print("Has guanyat el joc. Enhorabona!")
        print("***********************************")
        break

    #En este condicional si el usuario tiene la buena suerte de que toque el número que he establecido en el programa. Encontrará un Oasis.
    #Lo que permite el Oasis será restablecer los Tragos de la cantimplora es 10, la sed se restaurará a 0 y vuelve a empezar desde 0 de forma positiva ya que
    #Los kilómetros se mantendrán intactos al igual que la de los cazadores.
    if trobarOasi == 5:
        print("\n*************************************************************************************************************************")
        print(f"Enhorabona... Has trobat un Oasis justament t'ha sortit el número guanyador que era {trobarOasi} Tindrás una recompensa")
        print(f"\nOmplim els Galops de la cantimplora al total de nou. Els regenerarem al màxim permés")
        glopsCantimplora = 10
        print(f"\nRegenerarem la set del jugador al mínim que serà 0")
        set = 0
        print("\nL'Elefant descansarà i està molt content.")
        cansamentElefant = 0
        print("****************************************************************************************************************************")

    #Si la sed está entre 4 (superior) y 5 (incluido) mostrará el mensaje de alerta conforme el elefante tiene sed.
    if set > 4 and set <= 6:
        print("\n^^^^^^^^^^^^^^^^^^")
        print("Estàs assedegat")
        print("^^^^^^^^^^^^^^^^^^")
    #De lo contrario si la sed del elefante es superior a 6 el elefante habrá muerto de sed y terminará el juego.
    elif set > 6:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Has mort de set!... Has perdut!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        continuarBucle = False

    #Si el cansancio del elefante está entre 5 superior y 7 en este caso mostrará una alerta que dirá *El elefante se está cansando*
    if cansamentElefant > 5 and cansamentElefant <= 8:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("El teu elefant s'està cansant")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    #De lo contrario si el cansancio de elefante es superior a 8 el elefante morirá de cansancio. Y en este caso saldremos del bucle.
    elif cansamentElefant > 8:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("El teu elefant ha mort de cansament excesiu.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        continuarBucle = False

    #Si la distancia de los cazadores supera o es igual a los 15 kilòmetros saltará un aviso que dirá que los cazadores se acercan.
    if distanciaRecorregudaCacadors >= 15:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Els caçadors s'estan acostant!")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    #En este condicional comprobará que si los kilòmetros recorrdios - la distancia de los cazadores es menor o inferior a 0.
    #Entonces habrán atrapado al elefante.
    if kilometresRecorreguts - distanciaRecorregudaCacadors <=1:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Els Bosquiamanos t'han atrapat, Has perdut el joc!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        continuarBucle = False

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)