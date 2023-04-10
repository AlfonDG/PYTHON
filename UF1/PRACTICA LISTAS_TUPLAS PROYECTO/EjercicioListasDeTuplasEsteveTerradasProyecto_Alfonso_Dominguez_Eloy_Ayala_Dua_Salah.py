print('''
---------------------------------------------------------
Departament INS Esteve Terradas. Selección de Estudiantes
-------------------------------------------------------\n''')

print('''***** Selección de Idioma *****\n''')

idiomas = [(f"MENÚ PRINCIPAL CASTELLANO\n"
            "********************************************\n"
            "1. Añadir Alumno/Alumna\n"
            "2. Añadir Alumno/Alumna a Grupo de Proyecto\n"
            "3. Listar los grupos del proyecto\n"
            "4. Poner nota de proyecto\n"
            "5. Borrar Alumno/Alumna\n"
            "6. Calcular la media de las notas\n"
            "7. Salir de este menú\n"),(f"MENÚ PRINCIPAL EN CATALÀ\n"
            "********************************************\n"
            "1. Afegir Alumne\n"
            "2. Afegir Alumne a Grup de Projecte\n"
            "3. Llistar els grups del projecte\n"
            "4. Posar nota de projecte\n"
            "5. Borrar Alumne\n"
            "6. Calcular la mitjana de las notas\n"
            "7. Sortir d'aquest menú\n"),
           (f"MAIN MENU IN ENGLISH\n"
            "********************************************\n"
            "1. Add Student\n"
            "2. Add Student to join the grup project\n"
            "3. List all group members of the project\n"
            "4. Add qualification to the project\n"
            "5. Erase Student from the platform\n"
            "6. Calculate the median of the qualifications\n"
            "7. Exit this menu\n"),
           (f"MENU PRINCIPAL FRANÇAIS\n"
            "********************************************\n"
            "1. Ajouter un étudiant\n"
            "2. Ajouter un étudiant au groupe de projet\n"
            "3. Lister les groupes de projets\n"
            "4. Mettre la note de projet\n"
            "5. Supprimer l'élève\n"
            "6. Calculer la moyenne des notes\n"
            "7. Quittez ce menu\n"),(f"HAUPTMENÜ DEUTCHLAND\n"
            "********************************************\n"
            "1. Schüler hinzufügen\n"
            "2. Schüler zur Projektgruppe hinzufügen\n"
            "3. Projektgruppen auflisten\n"
            "4. Projektnotiz hinzufügen\n"
            "5. Schüler löschen\n"
            "6. Berechnen Sie den Durchschnitt der Noten\n"
            "7. Verlassen Sie dieses Menü\n"),
           ("f alqayimat alearabiat alrayiysiat \n"
            "********************************************** \n"
            "1. 'iidafat talib \n"
            "2. 'iidafat talib 'iilaa majmueat almashrue \n"
            "3. sard majmueat almashrue \n"
            "4. dae mulahazat almashrue \n"
            "5. hadhf altaalib \n"
            "6. ahsib mutawasit ​​aldarajat \n"
            "7. alkhuruj min hadhih alqayimat \n")]

menuIdiomas = True

while menuIdiomas == True:
    print(f"1. Castellano\n"
          "2. Catalán\n"
          "3. English\n"
          "4. Français\n"
          "5. Deutchland\n"
          "6. Arab\n"
          "7. Salir del Programa\n")

    escogerIdioma = int(input("Escriba el idioma que deseé que se le muestre el programa: "))
    print("")

    listaPersonas = []

    listaProyectos = []

    listaNotas = []

    sumaNotas = 0

    mediaNotas = 0

#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (CASTELLANO)
#------------------------------------------------------------------------------------------------------------------------
    if escogerIdioma == 1:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[0])

            seleccionarOpcion = int(input("Escriba la opción que deseé: "))

            print("")

            #Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                    numeroVeces = int(input("\nDiga el número de veces que quiera añadir alumnos: "))

                    print("")

                    for i in range(0,numeroVeces):

                        nombre = str(input("Introduzca el nombre del alumno/alumna: ")).capitalize()

                        apellido = str(input("Introduzca ahora el apellido del alumno/alumna: ")).capitalize()

                        poblacion = str(input("Introduzca la población en la que vive: ")).capitalize()

                        tuplaPersonas = (nombre,apellido,poblacion)

                        listaPersonas.append(tuplaPersonas)

                    print(f"\nHas añadidio los siguientes alumnos/alumnas -> {listaPersonas}\n")

            #Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("Escriba el nombre: ")).capitalize()

                        seleccionApellido = str(input("Escriba el apellido: ")).capitalize()

                        seleccionTituloProyecto = str(input("Escriba el nombre del proyecto: ")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print("Añadiremos el nombre del grupo y el nombre de los alumnos a la tupla de grupos unidos al proyecto\n")
                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"La tupla con la selección del título y los nombres del grupo serán -> {listaProyectos}\n")
                            menuGeneral = True
                        else:
                            print(f"No hemos encontrado el nombre ***{seleccionNombre}*** y el apellido ***{seleccionApellido}*** en nuestra lista de personas. La lista en formato tupla es {listaPersonas}\n")
                            menuIdiomas = False
                            menuGeneral = True

            #Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tTABLA DE GRUPOS Y ALUMNOS\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            #Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"Te mostramos a continuación el grupo nº {x + 1}:\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("Introduzca un grupo: ")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"Hemos encontrado el grupo. Has seleccionado el grupo {listaProyectos[i]}\n")
                            nota = float(input("Introduzca la nota a continuación: "))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("No hemos encontrado el grupo, te devolvemos al menú principal en Castellano.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas,"\n")

            #Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"No quedan alumnos en el proyecto {listaProyectos[i::]}... Por lo que procederemos a eliminar el grupo vacío\n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("Los grupos tienen sus respectivos alumnos. Procedemos a eliminar a un usuario del grupo\n")
                        elegirAlumnoBorrar = str(input("Introduzca el usuario que desea borrar: ")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"Hemos encontrado al alumno... {listaProyectos[i][1::]} Procedemos a borrarlo de la lista de proyectos")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"No hemos encontrado al alumno {elegirAlumnoBorrar} que has escrito")
                    print(listaProyectos,"\n")

            #Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:

                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"La media de las notas de los proyectos será igual a -> {mediaNotas}\n")

            #Salir del Programa en Castellano
            elif seleccionarOpcion == 7:
                print("Has decidido salir de este menú principal. Te devolvemos a la selección de idioma.\n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("No has introducido una opción adecuada. Saliendo del programa...")
#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (CATALÀ)
#------------------------------------------------------------------------------------------------------------------------
    elif escogerIdioma == 2:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[1])

            seleccionarOpcion = int(input("Escriu a continuacó l'opció que vulgui: "))

            print("")

            # Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                numeroVeces = int(input("\nDigues el número de vegades que vol afegir alumnes: "))

                print("")

                for i in range(0, numeroVeces):
                    nombre = str(input("Introdueix el nom del alumne/alumna ")).capitalize()

                    apellido = str(input("Introdueix a continuació el cognom dels alumnes: ")).capitalize()

                    poblacion = str(input("Introdueix la població en la que viu: ")).capitalize()

                    tuplaPersonas = (nombre, apellido, poblacion)

                    listaPersonas.append(tuplaPersonas)

                print(f"\nHas afegit els següents alumnes -> {listaPersonas}\n")

            # Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("Escriu un nom: ")).capitalize()

                        seleccionApellido = str(input("Escriu el cognom: ")).capitalize()

                        seleccionTituloProyecto = str(input("Escriu el nom del projecte: ")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print(" Afegirem el nom del grup i el nom del alumnes a la tupla de grups units al projecte\n")
                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"La tupla amb la sel·lecció del títol amb noms del grup seràn -> {listaProyectos}\n")
                            menuGeneral = True
                        else:
                            print(f"No hem pogut trobar ***{seleccionNombre}*** i el cognom ***{seleccionApellido}*** en la nostra llista de persones. La llista en format tupla és {listaPersonas}\n")
                            menuIdiomas = False
                            menuGeneral = True

            # Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tTAULES DE GRUPS I ALUMNES\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            # Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"Et mostrem a continuació el grup nº {x + 1}:\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("Introdueix el nom: ")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"Hem trobat el grup. Has sel·leccionat el grup {listaProyectos[i]}\n")
                            nota = float(input("Introdueix la nota a continuació: "))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("No hem trobat el grup, et retornem al menú principal en Català.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas, "\n")

            # Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"No queden alumnes en el projecte {listaProyectos[i::]}... Amb el que procedim a eliminar-los del grup vuit\n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("Els grup tienen els seus respectius alumnes. Procedim a eliminar un usuari del grup\n")
                        elegirAlumnoBorrar = str(input("Introdueix l'usuari a eliminar: ")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"Hem trobat el alumne... {listaProyectos[i][1::]} Procedim a suprimirlo de la llista de projectes")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"No hem pogut cercar l'alumne {elegirAlumnoBorrar} que has escrit")
                    print(listaProyectos, "\n")

            # Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:
                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"La mitjana de les notes de tots els projectes serà -> {mediaNotas}\n")

            # Salir del Programa en Català
            elif seleccionarOpcion == 7:
                print("Has decidit sortir del menú principal. Et retornem a la sel·lecció d'idiomes.\n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("No has introduït una opció adecuada. Sortint del programa...")

#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (ENGLISH)
#------------------------------------------------------------------------------------------------------------------------
    elif escogerIdioma == 3:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[2])

            seleccionarOpcion = int(input("Write the option you wanted: "))

            print("")

            # Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                numeroVeces = int(input("\nSay the number of times you want to add students: "))

                print("")

                for i in range(0, numeroVeces):
                    nombre = str(input("Enter the student's name: ")).capitalize()

                    apellido = str(input("Now enter the student's last name: ")).capitalize()

                    poblacion = str(input("Enter the city where you live: ")).capitalize()

                    tuplaPersonas = (nombre, apellido, poblacion)

                    listaPersonas.append(tuplaPersonas)

                print(f"\nYou have added the following students -> {listaPersonas}\n")

            # Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("Enter the name: ")).capitalize()

                        seleccionApellido = str(input("Enter last name: ")).capitalize()

                        seleccionTituloProyecto = str(input("Enter the project name: ")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print("We will add the name of the group and the name of the students to the tuple of groups joined to the project\n")

                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"The tuple with the selection of the title and the names of the group will be -> {listaProyectos}\n")
                            menuGeneral = True
                        else:
                            print(f"We did not find the name ***{seleccionNombre}*** and the last name ***{seleccionApellido}*** in our list of people. The list in tuple format is {listaPersonas}\n")
                            menuIdiomas = False
                            menuGeneral = True

            # Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tTABLE OF GROUPS AND STUDENTS\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            # Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"Then we show you the group nº {x + 1}:\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("Enter a group: ")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"We have found the group. You have selected the group {listaProyectos[i]}\n")
                            nota = float(input("Enter score below: "))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("We have not found the group, we return you to the main menu in Spanish.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas, "\n")

            # Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"There are no students left in the project {listaProyectos[i::]}... So we will proceed to eliminate the empty group\n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("The groups have their respective students. We proceed to remove a user from the group\n")
                        elegirAlumnoBorrar = str(input("Enter the user you want to delete: ")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"We have found the student... {listaProyectos[i][1::]} We proceed to delete it from the list of projects")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"We have not found the student {elegirAlumnoBorrar} that you have written")
                    print(listaProyectos, "\n")

            # Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:
                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"The average of the grades of the projects will be equal to -> {mediaNotas}\n")

            # Salir del Programa en English
            elif seleccionarOpcion == 7:
                print("You have decided to exit this main menu. We return you to the language selection.\n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("You have not entered a suitable option. Exiting the program...")

#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (FRANCÉS)
#------------------------------------------------------------------------------------------------------------------------
    elif escogerIdioma == 4:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[3])

            seleccionarOpcion = int(input("Écrivez l'option que vous vouliez : "))

            print("")

            # Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                numeroVeces = int(input("\nDites le nombre de fois que vous souhaitez ajouter des élèves : "))

                print("")

                for i in range(0, numeroVeces):
                    nombre = str(input("Entrez le nom de l'élève : ")).capitalize()

                    apellido = str(input("Entrez maintenant le nom de famille de l'élève : ")).capitalize()

                    poblacion = str(input("Entrez la ville où vous habitez : ")).capitalize()

                    tuplaPersonas = (nombre, apellido, poblacion)

                    listaPersonas.append(tuplaPersonas)

                print(f"\nVous avez ajouté les étudiants suivants -> {listaPersonas}\n")

            # Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("Entrez le nom : ")).capitalize()

                        seleccionApellido = str(input("Entrer le nom de famille: ")).capitalize()

                        seleccionTituloProyecto = str(input("Entrez le nom du projet : ")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print("Nous ajouterons le nom du groupe et le nom des étudiants au tuple des groupes joints au projet\n")
                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"Le tuple avec la sélection du titre et les noms du groupe sera -> {listaProyectos}\n")
                            menuGeneral = True
                        else:
                            print(f"Nous n'avons pas trouvé le prénom ***{seleccionNombre}*** et le nom ***{seleccionApellido}*** dans notre liste de personnes. La liste au format tuple est {listaPersonas}\n")
                            menuIdiomas = False
                            menuGeneral = True

            # Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tTABLE DES GROUPES ET ÉTUDIANTS\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            # Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"Ensuite, nous vous montrons le groupe nº {x + 1} :\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("Entrez un groupe : ")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"Nous avons trouvé le groupe. Vous avez sélectionné le groupe {listaProyectos[i]}\n")
                            nota = float(input("Entrez la note ci-dessous : "))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("Nous n'avons pas trouvé le groupe, nous vous renvoyons au menu principal en français.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas, "\n")

            # Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"Il n'y a plus d'élèves dans le projet {listaProyectos[i::]}... Nous allons donc procéder à l'élimination du groupe vide\n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("Les groupes ont leurs élèves respectifs. Nous procédons à la suppression d'un utilisateur du groupe\n")
                        elegirAlumnoBorrar = str(input("Entrez l'utilisateur que vous souhaitez supprimer : ")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"Nous avons trouvé l'étudiant... {listaProyectos[i][1::]} Nous le supprimons de la liste des projets")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"Nous n'avons pas trouvé l'étudiant {elegirAlumnoBorrar} que vous avez écrit")
                    print(listaProyectos, "\n")

            # Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:
                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"La moyenne des notes sera égale à -> {mediaNotas}\n")

            # Salir del Programa en Francés
            elif seleccionarOpcion == 7:
                print("Vous avez décidé de quitter ce menu principal. Nous vous ramenons à la sélection de la langue.\n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("Vous n'avez pas entré d'option appropriée. Quitter le programme...")

#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (ALEMÁN)
#------------------------------------------------------------------------------------------------------------------------
    elif escogerIdioma == 5:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[4])

            seleccionarOpcion = int(input("Schreiben Sie die gewünschte Option: "))

            print("")

            # Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                numeroVeces = int(input("\nSagen Sie, wie oft Sie Schüler hinzufügen möchten: "))

                print("")

                for i in range(0, numeroVeces):
                    nombre = str(input("Geben Sie den Namen des Schülers ein: ")).capitalize()

                    apellido = str(input("Geben Sie nun den Nachnamen des Schülers ein: ")).capitalize()

                    poblacion = str(input("Geben Sie die Stadt ein, in der Sie leben: ")).capitalize()

                    tuplaPersonas = (nombre, apellido, poblacion)

                    listaPersonas.append(tuplaPersonas)

                print(f"\nSie haben die folgenden Schüler hinzugefügt -> {listaPersonas}\n")

            # Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("Geben Sie den Namen ein: ")).capitalize()

                        seleccionApellido = str(input("Nachnamen eingeben: ")).capitalize()

                        seleccionTituloProyecto = str(input("Geben Sie den Projektnamen ein: ")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print("Wir fügen den Namen der Gruppe und den Namen der Schüler dem Tupel der Gruppen hinzu, die dem Projekt beigetreten sind\n")
                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"Das Tupel mit der Auswahl des Titels und der Namen der Gruppe wird -> {listaProyectos}\n")
                            menuGeneral = True
                        else:
                            print(f"Wir haben den Vornamen ***{seleccionNombre}*** und den Nachnamen ***{seleccionApellido}*** nicht in unserer Personenliste gefunden. Die Liste im Tupelformat ist {listaPersonas}\n")
                            menuIdiomas = False
                            menuGeneral = True

            # Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tTABELLE DER GRUPPEN UND SCHÜLER\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            # Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"Dann zeigen wir Ihnen die Gruppe Nr. {x + 1}:\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("Geben Sie eine Gruppe ein: ")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"Wir haben die Gruppe gefunden. Sie haben die Gruppe {listaProyectos[i]} ausgewählt\n")
                            nota = float(input("Notiz unten eingeben: "))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("Wir haben die Gruppe nicht gefunden, wir kehren zum Hauptmenü auf Deutch zurück.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas, "\n")

            # Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"Es sind keine Schüler mehr im Projekt {listaProyectos[i::]}... Also werden wir fortfahren, die leere Gruppe zu eliminieren\n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("Die Gruppen haben ihre jeweiligen Schüler. Wir fahren fort, einen Benutzer aus der Gruppe zu entfernen\n")
                        elegirAlumnoBorrar = str(input("Geben Sie den Benutzer ein, den Sie löschen möchten: ")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"Wir haben den Schüler gefunden... {listaProyectos[i][1::]} Wir fahren fort, ihn aus der Liste der Projekte zu löschen")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"Wir haben den von Ihnen geschriebenen Schüler {elegirAlumnoBorrar} nicht gefunden")
                    print(listaProyectos, "\n")

            # Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:
                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"Der Durchschnitt der Noten ist gleich -> {mediaNotas}\n")

            # Salir del Programa en Deutch
            elif seleccionarOpcion == 7:
                print("Sie haben sich entschieden, dieses Hauptmenü zu verlassen. Wir kehren zur Sprachauswahl zurück.\n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("Sie haben keine passende Option eingegeben. Beenden des Programms...")

#------------------------------------------------------------------------------------------------------------------------
    #Selección de Idioma en (ÁRABE)
#------------------------------------------------------------------------------------------------------------------------
    elif escogerIdioma == 6:

        menuIdiomas = False

        menuGeneral = True

        while menuGeneral == True:

            print(idiomas[5])

            seleccionarOpcion = int(input("aktub alkhiar aladhi turiduhu:"))

            print("")

            # Añadir alumnos a una tupla y luego a una lista para más tarde poder añadir los valores que deseemos.
            if seleccionarOpcion == 1:

                numeroVeces = int(input("\n qul eadad almaraat alati turid fiha 'iidafat tulaabi:"))

                print("")

                for i in range(0, numeroVeces):
                    nombre = str(input("'adkhil asm altaalb:")).capitalize()

                    apellido = str(input("'adkhal alan aliasm al'akhir liltaalba:")).capitalize()

                    poblacion = str(input("'adkhal almadinat alati taeish fiha:")).capitalize()

                    tuplaPersonas = (nombre, apellido, poblacion)

                    listaPersonas.append(tuplaPersonas)

                print(f"\nlaqad qumt bi'iidafat altulaab altaaliayn -> {listaPersonas}\n")

            # Selección de nombres y añadirlos a un grupo de proyecto.
            elif seleccionarOpcion == 2:

                numeroAlumnos = len(listaPersonas)

                print("")

                while numeroAlumnos >= len(listaPersonas):
                    for nombre, apellido, poblacion in listaPersonas:

                        seleccionNombre = str(input("'adkhal aliasm:")).capitalize()

                        seleccionApellido = str(input("'iidkhal asm akhir: ")).capitalize()

                        seleccionTituloProyecto = str(input("'adkhil asm almashruei:")).capitalize()

                        if seleccionNombre == nombre or seleccionApellido == apellido:
                            print("sanudif asm almajmueat wasm altulaab 'iilaa majmueat almajmueat almundamat 'iilaa almashrue \n")
                            tuplaGruposProyecto = (seleccionTituloProyecto, seleccionNombre)
                            listaProyectos.append(tuplaGruposProyecto)
                            numeroAlumnos -= 1
                            print(f"satakun almajmueat mae tahdid aleunwan wa'asma' almajmueat -> {listaProyectos} \n")
                            menuGeneral = True
                        else:
                            print(f"lim naethur ealaa aliasm al'awal *** {seleccionNombre} *** waliasm al'akhir *** {seleccionApellido} *** fi qayimat al'ashkhas ladina. alqayimat bitansiq tuple hi {listaPersonas} \n")
                            menuIdiomas = False
                            menuGeneral = True

            # Mostrar los grupos en formato tabla:
            elif seleccionarOpcion == 3:
                for i in listaProyectos:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
                          "-\t\t\t\tjadwal almajmueat waltulaab\t\t\t\t\t\n"
                          "-\n"
                          "-\n"
                          "\t\t\t\t--------------------"
                          "-\t\t\t\t\t"
                          "-\n"
                          f"-\t\t\t\t{i[0::2]} -> {i[1::]}\n"
                          "\t\t\t\t--------------------"
                          f"-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                          "-\n"
                          "-\n"
                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    menuGeneral = True
            # Establecer una nota al proyecto del grupo que el usuario quiera seleccionar.
            elif seleccionarOpcion == 4:

                numeroGrupos = len(listaProyectos)

                while numeroGrupos >= len(listaPersonas):

                    for x in range(len(listaProyectos)):
                        print(f"thuma naerid lak almajmueat nº {x + 1}:\n{listaProyectos[x][0]} -> {listaProyectos[x][1]}\n")

                    for i in range(len(listaProyectos)):
                        seleccionGrupo = str(input("'adkhal majmueata:")).capitalize()

                        if seleccionGrupo == listaProyectos[i][0] or seleccionGrupo == listaProyectos[1][i]:
                            print(f"laqad wajadna almajmueata. laqad hudidat almajmuea {listaProyectos[i]} \n")
                            nota = float(input("'adkhal almulahazat 'adnahu:"))
                            listaTempNotas = []
                            listaTempNotas.append(listaProyectos[i])
                            listaTempNotas.append(nota)
                            listaNotas.append(listaTempNotas)
                        else:
                            print("lam naethur ealaa almajmueat , narjieukum 'iilaa alqayimat alrayiysiat biallughat alearabiati.\n")
                            menuGeneral = False
                            menuIdiomas = True
                    numeroGrupos -= 1
                print(listaNotas, "\n")

            # Eliminar alumno del grupo y de la lista de personas.
            elif seleccionarOpcion == 5:
                for i in range(len(listaProyectos)):
                    if len(listaProyectos[i]) < 2:
                        print(f"lam yatabaqa 'ayu tulaab fi almashrue {listaProyectos[i::]} ... lidha sanashrae fi altakhalus min almajmueat alfarighat \n")
                        del listaProyectos[i]
                        print(listaProyectos)
                    else:
                        print("almajmueat laha tulaabuha. nantaqil 'iilaa 'iizalat mustakhdam min almajmueat\n")
                        elegirAlumnoBorrar = str(input("'udkhil almustakhdim aladhi turid hadhfahu:")).capitalize()

                        if elegirAlumnoBorrar in listaProyectos[i]:
                            print(f"laqad wajadna altaalib ... {listaProyectos[i][1::]} nantaqil 'iilaa hadhfih min qayimat almashariei")
                            for j in range(len(listaProyectos[i])):
                                listaTempTuplas = list(list(listaProyectos[i]))
                                del listaTempTuplas[i]
                                tuplaTempAnadirLista = tuple(listaTempTuplas)
                                print(tuplaTempAnadirLista)
                                listaProyectos[i] = tuplaTempAnadirLista
                        else:
                            print(f"No hemos encontrado al alumno {elegirAlumnoBorrar} que has escrito")
                    print(listaProyectos, "\n")

            # Calcular la media de todas las notas de los grupos en global.
            elif seleccionarOpcion == 6:
                sumaNotas = 0

                for i in range(len(listaNotas)):
                    todasLasNotas = listaNotas[i][1]
                    sumaNotas += todasLasNotas
                    mediaNotas = sumaNotas / len(listaNotas)
                print(f"sayakun mutawasit almulahazat yusawy -> {mediaNotas}\n")

            # Salir del Programa en Árabe
            elif seleccionarOpcion == 7:
                print("laqad qararat alkhuruj min hadhih alqayimat alrayiysiati. nueiduk 'iilaa akhtiar allughati. \n")
                menuGeneral = False
                menuIdiomas = True
            else:
                print("lam tadkhul alkhiar almunasibi. alkhuruj min albarnamaj ...")

    else:
        print("\n***No has seleccionado un idioma correcto o no está disponible.***")
        print("\n***No heu seleccionat un idioma correcte o no està disponible.***")
        print("\n***You have not selected a correct language or it is not available.***")
        print("\n ***lam tuhadid lughatan sahihatan 'aw 'anaha ghayr mutawafiratin.***")
        print("\n***Sie haben keine richtige Sprache ausgewählt oder sie ist nicht verfügbar.***")
        print("\n***Vous n'avez pas sélectionné une langue correcte ou elle n'est pas disponible.***")
        print()
        menuIdiomas = False

print("")
autor = __author__ = "Eloy Ayala | Dua Salah | Alfonso Domínguez"
copy = __copyright__="Copyright © 2022 Eloy Ayala | Dua Salah | Alfonso Domínguez Team"

print(autor)
print(copy)