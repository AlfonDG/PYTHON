__author__ = "Unax, Lucas & Alfonso"
__copyright__="Copyright © 2023 Unax, Lucas & Alfonso"

#A partir de aquí empieza el código del ejercicio.

#Establecemos los margenes del menú principal, título y las opciones en una lista
margenesMenu = "=" * 40

tituloMenuPrincipal = "MENÚ PRINCIPAL"

listaOpciones = ["A.- Introduir un milionari nou des de Teclat.","B.- Introduir la informació d’una empresa.",
                 "C.- Mostrar per pantalla la informació de tots els Milionaris.","D.- Mostrar milionari més ric.",
                 "E.- Modificar la informació d’un milionari","X.- Salir del Programa"]

#Aquí mostramos la lista vacía que irá el usuario rellenando a medida que vaya poniendo las opciones en el menú
listaDiccionarioMillonarios = []

#Aquí establecemos las accionesEmpresa con el nombre de las respectivas empresas con el valor de las acciones
accionesEmpresa = {"MicroSopa":2.67,"AireTel": 1.2,"AmenizaDos": 0.98,"IbemePorUvas": 5.3,"MacChiton": 0.25}

menuContinuar = True

#Ahora crearemos la primera función de Menú Principal que printará las opciones del menú y la opción a seleccionar.
def menuPrincipal(menuContinuar):

    while menuContinuar == True:

        print("\n",tituloMenuPrincipal.rjust(25))
        print(margenesMenu)

        for i in range(len(listaOpciones)):

            print(listaOpciones[i])

        opcionEscoger = str(input("\nIntroduzca la letra acorde a la opción: ")).upper()

        #El usuario puede escoger uno de entre estos valores para que llame a una función en concreto.
        if opcionEscoger == "A":

            millonari_nou(listaDiccionarioMillonarios, accionesEmpresa)

        elif opcionEscoger == "B":

            introduir_nova_empresa(accionesEmpresa)

        elif opcionEscoger == "C":

            mostrar_tots_millonaris(listaDiccionarioMillonarios)

        elif opcionEscoger == "D":

            print(millonari_mes_ric(listaDiccionarioMillonarios, accionesEmpresa))

        elif opcionEscoger == "E":

            subMenu_Edicion_Millonario(listaDiccionarioMillonarios,menuContinuar)

        elif opcionEscoger == "X":

            sortir_del_programa()

            menuContinuar = False

        else:
            print("\n¡¡¡¡No has introducido una opción adecuada. Saldremos del menú principal!!!!")

            menuContinuar = False

#Esta función creará y añadirá un nuevo millonario a la listaDiccionarioMillonario
def millonari_nou(listaDiccionarioMillonarios,accionesEmpresa):

    nVeces = int(input("\nNúmero de veces que desea añadir millonario: "))

    for i in range(0, nVeces):

        listaAcconesEmpresarios = []

        nombreMillonario = str(input("\nIntroduzca el nombre del millonario: ")).capitalize()

        edadMillonario = int(input("Introduzca la edad del millonario: "))

        for keysAcciones in accionesEmpresa.keys():

            #En este caso el usuario tendrá que establecer solamente números
            cantidadesAcciones = input("Cuántas acciones tiene el empresario: ")

            print(f"Para la empresa {keysAcciones} has añadido un total de {cantidadesAcciones} acciones")

            if len(cantidadesAcciones) == 0:

                listaAcconesEmpresarios.append(0)

            elif cantidadesAcciones.isalpha() and cantidadesAcciones.isalnum():

                print("\nDebes de escribir un número, no puede ser una string o un nombre")

                break

            else:
                listaAcconesEmpresarios.append(cantidadesAcciones)

        listaDiccionarioMillonarios.append({"nombreMillonario": nombreMillonario, "edadMillonario": edadMillonario,"accionesMillonarioPorEmpresa": listaAcconesEmpresarios})

    print(listaDiccionarioMillonarios)

#En esta otra función mostrará el millonario más rico ordenado por el método burbuja
def millonari_mes_ric(listaDiccionarioMillonarios,accionesEmpresa):

    # Crearemos las listas vacías para poder almacenar por separados y en listas los valores
    listaAccionesEmpresas = []

    totalAccionesPorMillonario = []

    listaNombresMillonarios = []

    #En este FOR loop almacenamos los valores de las acciones de cada empresa y las guardará en una lista vacía
    for valoresAccionesEmpresas in accionesEmpresa.values():

        listaAccionesEmpresas.append(valoresAccionesEmpresas)

    #Con este FOR loop calculamos el total de cada acción por millonario y multiplicaremos ese resultado por cada acción de la empresa y así obtendremos el resultado
    for keysMillonarios in listaDiccionarioMillonarios:

        listaNombresMillonarios.append(keysMillonarios["nombreMillonario"])

        suma = 0

        for i in range(len(listaAccionesEmpresas)):
            suma += float(listaAccionesEmpresas[i]) * float(keysMillonarios["accionesMillonarioPorEmpresa"][i])

        totalAccionesPorMillonario.append(suma)

    for i in range(len(totalAccionesPorMillonario)):

        for j in range(len(totalAccionesPorMillonario)-1):

            if totalAccionesPorMillonario[j] > totalAccionesPorMillonario[j + 1]:

                auxiliarAcciones = totalAccionesPorMillonario[j]

                totalAccionesPorMillonario[j] = totalAccionesPorMillonario[j + 1]

                totalAccionesPorMillonario[j + 1] = auxiliarAcciones

                auxiliarNombres = listaNombresMillonarios[j]

                listaNombresMillonarios[j] = listaNombresMillonarios[j + 1]

                listaNombresMillonarios[j + 1] = auxiliarNombres

    return f"\nEl millonario más rico será ***{listaNombresMillonarios[i]}*** tine un total de ***{totalAccionesPorMillonario[i]}*** millones de euros en acciones"

#En la función mostrar todos los millonarios mostrará todos los millonarios por su nombre y la edad que tienen
#de forma ordenada ya que la ordena por edad de más joven a más mayor
def mostrar_tots_millonaris(listaDiccionarioMillonarios):

    listaEdadesOrdenadas = []

    listaEdadesYNombresOrdenados = []

    for keysMillonarios in listaDiccionarioMillonarios:

        nombreMillonario = keysMillonarios["nombreMillonario"]

        edadMillonario = keysMillonarios["edadMillonario"]

        listaEdadesOrdenadas.append((nombreMillonario, edadMillonario))

        listaEdadesYNombresOrdenados = listaEdadesOrdenadas

    listaEdadesYNombresOrdenados.reverse()

    print(listaEdadesYNombresOrdenados)

    for nombreMillonario, edadMillonario in listaEdadesYNombresOrdenados:

        print(f"La lista Ordenada de edades será -> nombre: {nombreMillonario}  edad: {edadMillonario}")

#En esta función añadirá a una nueva empresa. Tantas como el usuario crea conveniente y a su vez
#esta función comprobará que si la empresa existe... O tiene el mismo nombre NO la añadirá pero si no la encuentra la añadirá
#a la lista de empresasAcciones
def introduir_nova_empresa(accionesEmpresa):

    numEmpresas = int(input("\nIntroduzca el máximo valor de empresas que desea añadir: "))

    nombreEmpresaIgual = False

    for i in range(0,numEmpresas):

        nombreEmpresa = str(input("\nIntroduzca el nombre de la nueva empresa: ")).strip().title()

        nombreEmpresa = nombreEmpresa.replace(" ","")

        valorAccionesEmpresa = float(input("Introduzca ahora el valor de sus acciones para dicha empresa: "))

        for keysAcciones,valorAcciones in accionesEmpresa.items():

            if nombreEmpresa == accionesEmpresa[keysAcciones]:

                nombreEmpresaIgual = True

                print(f"Ya existe una empresa con el mismo nombre ***{keysAcciones}***, no la añadiremos al diccionario. Le devolvemos al menú principal")

                menuSeguir = True

                break

        if nombreEmpresaIgual == False:

            print("\nAñadiendo una nueva empresa al diccionario de accionesEmpresas...\n")

            accionesEmpresa[nombreEmpresa] = valorAccionesEmpresa

    print(accionesEmpresa)

def subMenu_Edicion_Millonario(listaDiccionarioMillonarios,menuContinuar):

    tituloSubMenu = "SUB MENÚ PRINCIPAL"

    margenesSubMenu = "*" * 50

    opcionesSubmenu = ["1. Modificar Nombre Millonario",
                       "2. Modificar las Acciones que tenga por Empresa el Millonario",
                       "3. Modificar la edad del millonario",
                       "4. Salir del Sub Menú"]

    submenuContinuar = True

    while submenuContinuar == True:

        print("\n", tituloSubMenu.rjust(30))
        print(margenesSubMenu)

        for i in opcionesSubmenu:
            print(i)

        print(margenesSubMenu)

        introducirNumeroSubMenu = int(input("\nIntroduzca un número para seleccionar el dato que desea modificar: "))

        if introducirNumeroSubMenu == 1:

            nombreMillonarioRepetido = True

            introducirNombreMillonario = str(
                input("\nEscriba el nombre del millonario en el diccionario: ")).capitalize()

            introducirNombreACambiar = str(
                input("Introduzca el nuevo nombre del millonario a modificar: ")).capitalize()

            nombreMillonario = ""

            for keyMillonario in listaDiccionarioMillonarios:

                nombreMillonarios = keyMillonario["nombreMillonario"]

                if introducirNombreACambiar == nombreMillonarios:
                    print(
                        f"\nEl nombre del millonario que ha introducido ya existe, se llama {nombreMillonarios}. No cambiaremos este nombre y le devolvemos al SUB MENÚ")

                    nombreMillonarioRepetido = False

                if nombreMillonarios == introducirNombreMillonario:
                    nombreMillonario = keyMillonario

            if nombreMillonarioRepetido == True:
                nombreMillonario["nombreMillonario"] = introducirNombreACambiar

                submenuContinuar = True

            print("\n", listaDiccionarioMillonarios)


        elif introducirNumeroSubMenu == 2:

            print("Te mostramos a continuación el nombre de todas las empresas y las acciones que hay en cada una:\n")

            for keysAcciones, valoresAcciones in accionesEmpresa.items():
                print(keysAcciones, end=" -> ")

                print(valoresAcciones)

            seleccionarEmpresa = str(

                input("\nIntroduzca la empresa con la que desea trabajar y modificar del usuario: "))

            seleccionarEmpresa = seleccionarEmpresa.replace(" ", "")

            accionIndex = 1

            if seleccionarEmpresa in list(accionesEmpresa.keys()):
                accionIndex = list(accionesEmpresa.keys()).index(seleccionarEmpresa)

            Empresa_selecionada = False

            for acciones in listaDiccionarioMillonarios:

                if acciones["accionesMillonarioPorEmpresa"] == seleccionarEmpresa:
                    Empresa_selecionada = True

            for i, millonario in enumerate(listaDiccionarioMillonarios):
                print(f"{i + 1}.{millonario['nombreMillonario']}", end=",")

            # Pedir al usuario que seleccione el millonario que desea modificar la acción

            millonarioIndex = int(input("Ingrese el usuario millonario que desea modificar: "))

            # Verificar si el usuario millonario es válido

            if accionIndex < 0 or millonarioIndex >= len(listaDiccionarioMillonarios):
                print("El índice del millonario no es válido.")

                continue

            millonario = listaDiccionarioMillonarios[millonarioIndex - 1]

            # Pedir al usuario que ingrese el nuevo valor de la acción

            nuevoValorAccion = int(input("Ingrese el nuevo valor de la acción: "))

            millonario["accionesMillonarioPorEmpresa"][accionIndex] = nuevoValorAccion

            print("La acción ha sido modificada exitosamente.")

            print(listaDiccionarioMillonarios[millonarioIndex - 1])

        elif introducirNumeroSubMenu == 3:

            nombreMillonarioEncontradoEdad = False

            introducirNombreMillonario = str(input("\nIntroduzca el nombre del millonario al cual desea modificar la edad: ")).capitalize()

            for keysMillonarios in listaDiccionarioMillonarios:

                nombreMillonario = keysMillonarios["nombreMillonario"]

                edadMillonario = keysMillonarios["edadMillonario"]

                if introducirNombreMillonario == nombreMillonario:

                    print(f"Hemos encontrado el nombre del millonario llamado {nombreMillonario}. Modifique ahora su edad")

                    nombreMillonarioEncontradoEdad = True

                    introducidEdadACambiar = int(input(f"\nNueva edad para este millonario: "))

                    keysMillonarios["edadMillonario"] = introducidEdadACambiar

                if nombreMillonarioEncontradoEdad == False:

                    print(f"\nLo siento pero no hemos encontrado el nombre del millonario llamado {introducirNombreMillonario}. Le devolvemos al sub menú")

                    submenuContinuar = True

            print("\n",listaDiccionarioMillonarios)

        elif introducirNumeroSubMenu == 4:

            print("\nOk, saliendo del Sub Menú al Menú Principal")

            submenuContinuar = False

            menuContinuar = True

        else:
            print("\nNo ha introducido una opción de menú adecuada. Volvemos al menú principal")

            return menuContinuar

#Función de salida de programa. Directamente tiene harcodeado un menuContinuar = False en caso de que el usuario pique esta opción
#Saldrá del programa
def sortir_del_programa():

    print("\nOk, Saldremos del programa...")

menuPrincipal(menuContinuar)

print("")

print(__author__)
print(__copyright__)
