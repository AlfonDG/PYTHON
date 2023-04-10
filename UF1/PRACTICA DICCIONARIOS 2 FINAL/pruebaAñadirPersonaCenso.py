import random

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

    if sexoPersona != "H" and sexoPersona != "M" and sexoPersona != "I":
        print(f"\n!!!!Error, el sexo de la persona no es ninguna de las siguientes opciones -> *H*,*M* o bien *I*, usted ha escrito -> {sexoPersona}!!!")
        menuSeguir = False
        break


    elif edadPersona <= 0 or edadPersona > 100:
        print("\n!!!Error, no puede ser un valor superior a 100 años o inferior a 0 años!!!")
        menuSeguir = False
        break

    elif categoriaPersona != "pueblo" and categoriaPersona != "césar" and categoriaPersona != "soldado" and categoriaPersona != "centurión" and categoriaPersona is not categoriaPersona.isalpha():
        print("\n!!!Error, la categoría que has introducido no cumple los siguientes requisitos: Ha de ser categoría de tipo *peublo*,*césar*,*soldado*,*centurión* o bien *peublo*.\n"
            ,"Otro problema que hemos encontrado es que has intentado añadir números o carácteres raros a la categoría. Eso no es correcto ha de ser solamente letras.")
        menuSeguir = False
        break

    elif len(idPersonaAnadir) < len(idPersonas) or idPersonaAnadir == idPersonas:
        print("\nError. No podemos añadir a la persona ya que el Identificado coincide con uno de los que ya hay añadidos en el Censo del Imperio Romano o bien ha superado la longitud de valores.")
        menuSeguir = False
        break

    elif categoriaPersona == "césar" or vecesCategoriaCesar > 1:
        print("\nHemos detectado que hay más de un César o has intentado añadir esta categoría habiendo ya un César censado en el Censo del Imperio Romano\n")
        menuSeguir = False
        break

for idPersonas, valoresGeneralesPersonas in censoImperio.items():

    nombresCenso = valoresGeneralesPersonas["nombre"]

    if nombrePersona == nombresCenso:
        print("\nYa se ha añadido este nombre en el diccionario. Volveremos al menú principal.")
        menuSeguir = False

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