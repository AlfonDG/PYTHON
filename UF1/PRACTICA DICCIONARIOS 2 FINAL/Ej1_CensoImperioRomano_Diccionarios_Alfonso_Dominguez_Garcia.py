import random

import sys

censoImperio={
"AR1":{"nombre":"Claudia","region":"Roma","edad":23,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"AD3":{"nombre":"Maximo","region":"Hispania","edad":30,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AC2":{"nombre":"Marco","region":"Hispania","edad":28,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AV6":{"nombre":"Julius","region":"Roma","edad":35,"sexo":"H","categoría":"césar","fuerza":random.uniform(50,200)},
"SS5":{"nombre":"Augustus","region":"Hispania","edad":21,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"WQ6":{"nombre":"Eugenia","region":"Hispania","edad":28,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"JU8":{"nombre":"Anastacia","region":"Hispania","edad":17,"sexo":"I","categoría":"soldado","fuerza":random.uniform(50,200)},
"DF5":{"nombre":"Aurelia","region":"Hispania","edad":20,"sexo":"M","categoría":"pueblo","fuerza":random.uniform(50,200)},
"BR1":{"nombre":"Antistia","region":"Roma","edad":16,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"KR9":{"nombre":"Apolonia","region":"Roma","edad":25,"sexo":"I","categoría":"centurión","fuerza":random.uniform(50,200)},
"KH7":{"nombre":"Acucia","region":"Roma","edad":29,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"XH4":{"nombre":"Titus","region":"Roma","edad":39,"sexo":"I","categoría":"pueblo","fuerza":random.uniform(50,200)},
"KA2":{"nombre":"Aurelio","region":"Roma","edad":15,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
"MJ8":{"nombre":"Tiberius","region":"Roma","edad":22,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
}

fuerza = 0

menuSeguir = True

while menuSeguir == True:

    datos = ("1. Añadir persona en el Censo", "2. Buscar a la persona en el Censo", "3. Mostrar soldados de Hispania",
             "4. Visualizar la categoría del Censo")

    titulo = "CENSO ROMANO"

    cabecera = "_" * 30

    print("\n",titulo.center(30), "\n", cabecera)

    for i in datos:
        print(i)
    print("")

    escogerOpcion = int(input("Introduzca la opción que deseé: "))

    if escogerOpcion == 1:

        nombrePersona = str(input("\nIntroduzca el nombre de la persona que desea añadir: ")).capitalize()

        sexoPersona = str(input("\nIntroduzca el sexo de la persona que desea añadir. Solamente podrá establecer (M ,H o I): ")).upper()

        regionPersona = str(input("\nIntroduzca la región de la persona a añadir: ")).capitalize()

        edadPersona = int(input("\nIntroduzca un valor de edad para la persona que desea añadir: "))

        categoriaPersona = str(input("\nIntroduzca la categoría de la persona que desea añadir: ")).lower()

        fuerzaPersona = random.uniform(50, 200)

        idPersonaAnadir = str(input("\nAñada finalmente el ID de la persona que se encontrará en el Censo del Imperio Romano: ")).upper()

        for idPersonas, valoresGeneralesPersonas in censoImperio.items():

            nombresCenso = valoresGeneralesPersonas["nombre"]

            regionCenso = valoresGeneralesPersonas["region"]

            edadCenso = valoresGeneralesPersonas["edad"]

            sexosCenso = valoresGeneralesPersonas["sexo"]

            categoriasCenso = valoresGeneralesPersonas["categoría"]

            fuerzasCenso = valoresGeneralesPersonas["fuerza"]

            vecesCategoriaCesar = categoriasCenso.count("césar")

            if len(nombrePersona) <= 0:
                print(f"\n!!!Error, no has escrito un nombre adecuado o has escrito números en el nombre. Solamente pueden ser letras!!!")
                sys.exit()

            elif sexoPersona != "H" and sexoPersona != "M" and sexoPersona != "I":
                print(f"\n!!!!Error, el sexo de la persona no es ninguna de las siguientes opciones -> *H*,*M* o bien *I*, usted ha escrito -> {sexoPersona}!!!")
                sys.exit()

            elif edadPersona <= 0 or edadPersona > 100:
                print("\n!!!Error, no puede ser un valor superior a 100 años o inferior a 0 años!!!")
                sys.exit()

            elif categoriaPersona != "pueblo" and categoriaPersona != "césar" and categoriaPersona != "soldado" and categoriaPersona != "centurión" and categoriaPersona is not categoriaPersona.isalpha():
                print("\n!!!Error, la categoría que has introducido no cumple los siguientes requisitos: Ha de ser categoría de tipo *peublo*,*césar*,*soldado*,*centurión* o bien *peublo*.\n"
                    ,"Otro problema que hemos encontrado es que has intentado añadir números o carácteres raros a la categoría. Eso no es correcto ha de ser solamente letras.")
                sys.exit()

            elif len(idPersonaAnadir) < len(idPersonas) or idPersonaAnadir == idPersonas:
                print("\nError. No podemos añadir a la persona ya que el Identificado coincide con uno de los que ya hay añadidos en el Censo del Imperio Romano o bien ha superado la longitud de valores.")
                sys.exit()

            elif categoriaPersona == "césar" or vecesCategoriaCesar > 1:
                print("\nHemos detectado que hay más de un César o has intentado añadir esta categoría habiendo ya un César censado en el Censo del Imperio Romano\n")
                sys.exit()

        for idPersonas, valoresGeneralesPersonas in censoImperio.items():

            nombresCenso = valoresGeneralesPersonas["nombre"]

            if nombrePersona == nombresCenso:
                print("\nYa se ha añadido este nombre en el diccionario. Volveremos al menú principal.")
                sys.exit()

        # Añadir a Diccionario una nueva persona en caso de que las demás opciones se cumplan perfectamente.
        censoImperio[idPersonaAnadir] = {"nombre": nombrePersona, "region": regionPersona, "edad": edadPersona,"sexo": sexoPersona, "categoría": categoriaPersona, "fuerza": fuerzaPersona}

        # Bucle final para recorrer y printar todo el Censo del Imperio Romano de forma detallada
        contadorPersonas = 1
        margenContadorPersona = "-" * 18

        for clavesPrincipalesPersonas in censoImperio.keys():
            print("")
            print(margenContadorPersona)
            print(" Persona Nº: ", contadorPersonas)
            print(margenContadorPersona)
            contadorPersonas += 1
            print("IDPersona ->", clavesPrincipalesPersonas)
            for datosPersonas in censoImperio[clavesPrincipalesPersonas].values():
                print("···", datosPersonas, end=" \n")

        menuSeguir = True

    elif escogerOpcion == 2:

        introducirNombre = str(input("\nIntroduzca el nombre de la persona del Censo Romano: ")).capitalize()

        personaNoEncontrada = True

        personasCensoAcumuladas = ""

        clavesExcluidas = "fuerza"

        margenes = "-" * 70

        resultadoDatosPrint = "\n\t\t\t\t\t\t\tDATOS PEDIDOS\n" + margenes + "\n NOMBRE \t\t REGION \t\t EDAD \t\t SEXO \t\t CATEGORIA\n" + margenes + "\n"

        for idPersona, datosPersona in censoImperio.items():
            busquedaPersonas = datosPersona["nombre"]

            if introducirNombre.startswith(introducirNombre) == busquedaPersonas.startswith(introducirNombre):
                personaNoEncontrada = False
                for clavesPersonas in censoImperio[idPersona].keys():
                    if clavesPersonas != clavesExcluidas:
                        personasCensoAcumuladas += (str(censoImperio[idPersona][clavesPersonas]).ljust(15))
                personasCensoAcumuladas += "\n"

        if personaNoEncontrada == True:
            print(f"Error la persona de nombre ***{introducirNombre}*** no se encuentra dentro del Censo del Imperio Romano","\n")
        else:
            print(resultadoDatosPrint + personasCensoAcumuladas,"\n")

        menuSeguir = True

    elif escogerOpcion == 3:

        asteriscos = "*" * 70

        personasHispanasCensoAcumuladas = ""

        clavesExcluidas = "fuerza"

        datosSoldadosHispaniaCompletos = []

        menuSoldadosHispania = "\n\t\t\t\t\t\tSOLDADOS DE HISPANIA" + "\n" + asteriscos + "\n" + "\n NOMBRE \t\t REGION \t\t EDAD \t\t SEXO \t\t CATEGORIA\n" + asteriscos + "\n"

        personaNoEncontrada = True

        for idPersona, datosPersonas in censoImperio.items():

            regionHispania = datosPersonas["region"]

            categoriaSoldados = censoImperio[idPersona]["categoría"]

            if regionHispania == "Hispania" and categoriaSoldados == "soldado":
                personaNoEncontrada = False
                for clavesPersonas in censoImperio[idPersona].keys():
                    if clavesPersonas != clavesExcluidas:
                        personasHispanasCensoAcumuladas += (str(censoImperio[idPersona][clavesPersonas]).ljust(15))
                personasHispanasCensoAcumuladas += "\n"

        if personaNoEncontrada == True:
            print("No hemos encontrado a la persona en el Censo del Imperio Romano en la sección de personas Hispanas.")
        else:
            print(menuSoldadosHispania + personasHispanasCensoAcumuladas,"\n")

        menuSeguir = True

    #En este ejercicio se ha de ejecutar en orden las categorías.
    #Es decir si en el diccionario primero se ejecutará el centurión se ha de escribir centurión, si luego toca printar un soldado se ha de escribir soldado etc...
    elif escogerOpcion == 4:
        recuentoCategoriaCenturion = 0

        recuentoCategoriaSoldado = 0

        recuentoCategoriaPueblo = 0

        recuentoCategoriaCesar = 0

        categoriaIntroducir = str(input("\nIntroduzca la categoría que deseé ver en el Censo Romano: ")).lower()

        for datosPersona in censoImperio.values():

            categoriaCenso = datosPersona["categoría"]

            while categoriaIntroducir != categoriaCenso:
                categoriaIntroducir = str(input("\nIntroduzca la categoría que deseé ver en el Censo Romano: ")).lower()

            if categoriaCenso == categoriaIntroducir:

                if categoriaCenso == "centurión":

                    print("\n Nombre:", datosPersona["nombre"], "\n",
                          "Región:", datosPersona["region"], "\n",
                          "Edad:", datosPersona["edad"], "\n",
                          "Sexo:", datosPersona["sexo"], "\n",
                          "Categoría:", datosPersona["categoría"], "\n")
                    recuentoCategoriaCenturion += 1

                elif categoriaCenso == "soldado":
                    print("\n Nombre:", datosPersona["nombre"], "\n",
                          "Región:", datosPersona["region"], "\n",
                          "Edad:", datosPersona["edad"], "\n",
                          "Sexo:", datosPersona["sexo"], "\n",
                          "Categoría:", datosPersona["categoría"], "\n")
                    recuentoCategoriaSoldado += 1

                elif categoriaCenso == "césar":
                    print("\n Nombre:", datosPersona["nombre"], "\n",
                          "Región:", datosPersona["region"], "\n",
                          "Edad:", datosPersona["edad"], "\n",
                          "Sexo:", datosPersona["sexo"], "\n",
                          "Categoría:", datosPersona["categoría"], "\n")
                    recuentoCategoriaCesar += 1

                elif categoriaCenso == "pueblo":
                    print("\n Nombre:", datosPersona["nombre"], "\n",
                          "Región:", datosPersona["region"], "\n",
                          "Edad:", datosPersona["edad"], "\n",
                          "Sexo:", datosPersona["sexo"], "\n",
                          "Categoría:", datosPersona["categoría"], "\n")
                    recuentoCategoriaPueblo += 1

                pulsarTecla = input("Pulsa una tecla para continuar...\n")

        print(f"El recuento total de personas con categoría CENTURIÓN son -> {recuentoCategoriaCenturion}")
        print(f"El recuento total de personas con categoría CÉSAR son -> {recuentoCategoriaCesar}")
        print(f"El recuento total de personas con categoría PUEBLO son -> {recuentoCategoriaPueblo}")
        print(f"El recuento total de personas con categoría SOLDADO son -> {recuentoCategoriaSoldado}","\n")

        menuSeguir = True

    else:
        print("\n!!!No ha escogido una opción válida para poder seleccionar en el menú. Saliendo del programa...!!!")
        menuSeguir = False

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)