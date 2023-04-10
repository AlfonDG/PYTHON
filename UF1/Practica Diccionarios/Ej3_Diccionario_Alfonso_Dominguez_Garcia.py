menu = '''\t\t\t MENÚ AGENDA
        -----------------------------
        1. Añadir/Modificar Usuario
        2. Buscar Contactos
        3. Borrar Contacto
        4. Listar Contactos
        5. Salir del Programa
        -----------------------------'''

menuSeguir = True

agenda = {}

while menuSeguir == True:

    print(menu)

    seleccionOpcion = int(input("Escriba la opción que deseé del menú: "))

    print("")

    #Opción nº1--------------------------------------------------------------------
    if seleccionOpcion == 1:
        numPersonasAAnadir = int(input("Introduzca cuantos usuarios deseé: "))

        while numPersonasAAnadir > 0:
            dni = str(input("Introduzca el DNI de la persona: "))
            nombre = str(input("Introduzca el nombre de la persona: ")).title()
            numTelefono = int(input("Escriba el número de Teléfono: "))

            if dni in agenda.keys():
                print(f"Hemos encontrado el DNI {dni}... Desea actualizarlo?")
                actualizar = str(input("Escriba si es SI/NO o si/no")).lower()

                if actualizar == "si":
                    print("Vuelva a introducir sus datos")
                    volverNombreAnadir = str(input("Introduzca el nombre de la persona: ")).title()
                    volverNumTelefonoAnadir = int(input("Escriba el número de Teléfono: "))
                    agenda[dni] = [volverNombreAnadir,volverNumTelefonoAnadir]
                    print(f"Datos actualizados...\n{agenda}")
                elif actualizar == "no":
                    print("No actualizaremos sus datos, te devolvemos al menú principal")
                    menuSeguir = True
                else:
                    print("No has introducido una opción válida... Te devolvemos al menú principal")
                    menuSeguir = True
            else:
                print("No hemos encontrado el DNI. Procedemos a añadirlo")
                agenda[dni] = [nombre,numTelefono]
                print("")
            numPersonasAAnadir -= 1
        menuSeguir = True

    #Opción nº 2--------------------------------------------------------------------------------
    elif seleccionOpcion == 2:
        buscar = str(input("Introduzca el nombre que desea buscar en la agenda de contactos: ")).title()

        print("")

        valueFind = False

        for nombre, telefono in agenda.values():
            if nombre.startswith(buscar):
                print(f"Los nombres que empiezan por los carácteres {buscar:} son -> {nombre:^5} y su número de teléfono es {telefono:^5}\n")
                break
        if valueFind == False:
            print("No hemos encontrado el valor")
            print("Te devolvemos al menú principal\n")
        menuSeguir = True

    #Opción nº 3----------------------------------------------------------------------------------
    elif seleccionOpcion == 3:

        nombreBuscar = str(input("Escriba el nombre que deseé: ")).title()

        for dni, persona in agenda.items():
            if persona[0] == nombreBuscar:
                print(f"Hemos encontrado a la persona {nombreBuscar}, desea eliminarla? ")

                eliminar = str(input("Escriba si desea eliminar el nombre SI/NO: ")).lower()

                if eliminar == "si":
                    print("Procedemos a eliminar el contacto de la AGENDA DE CONTACTOS\n")
                    del agenda[dni]
                    # del agenda[dni] = [None,persona[1]] -> Esta opción comentada nos permite eliminar a la persona pero dejar su teléfonfo de contacto
                    print("Nombre de persona Eliminada")
                    break

                elif eliminar == "no":
                    print("No deseas eliminar a la persona... Por lo tanto te devolvemos al menú principal")
                    menuSeguir = True

                else:
                    print("No has introducido un nombre de forma adecuada\n")
                    menuSeguir = True
    #Opción nº 4 Listar los Contactos de la Agenda de Contactos
    elif seleccionOpcion == 4:

        for dni,contacto in agenda.items():

            print(f"Procedemos a mostrar/listar toda la AGENDA DE CONTACTOS a continuación\n")

            print("DNI".center(10),"\n",dni, "NOMBRE".ljust(15),"\n",contacto[0], "TELÉFONFO".rjust(10),"\n",contacto[1])

            #print(f"DNI \n{dni:^10}\t NOMBRE \n{contacto[0]:<15}\t TELÉFONO \n{contacto[1]:>10}\t")

            print("_"*50)

            print("")

            print("Te devolvemos al menú principal\n")

            break
        menuSeguir = True

    #Opción nº 5 Salimos del programa.
    elif seleccionOpcion == 5:

        print("Salimos del menú principal...")

        menuSeguir = False

    else:
        print("No has introducido una opción adecuada... Salimos del Programa")
        menuSeguir = False