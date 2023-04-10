alumnos = ["Pere","Pau","Anna","Andrea","Pol","Nil","Montserrat","Gerard"]

notas = [4.3, 5.6, 5.9, 9.7, 2.6, 6.8, 8.8, 2.4]

margenes = "=" * 60

tituloMenuPrincipal = "MENÚ ALUMNOS GESTIÓN DE NOTAS"

#Esta variable cadenaU hace referencia al apartado e) de la función encontrarNombreAlumno() ya que es una cadena que pediremos al usuario
#Préviamente a la entrada al menú principal.
cadenaU = str(input("Introduzca el nombre del alumno y le diremos si se encuentra en la lista: ")).capitalize()

def menuPrincipal():
    menuSeguir = True

    while menuSeguir == True:
        print("\n",tituloMenuPrincipal.rjust(38))
        print(margenes)
        print("a) Mostrar los nombres de alumnos que aprobaran el examen")
        print("b) Devolver el número de aprobados en el examen")
        print("c) Mostrar los dos estudiantes con la máxima nota")
        print("d) Mostrar el nombre de los alumnos que superen o igualen o superen la media")
        print("e) Buscar al estudiante en la lista de alumnos")
        print("f) Ordenar el nombre de los alumnos de máxima nota a mínima")
        print("g) Salir del Programa")
        print(margenes)
        print("")

        seleccionOpcion = str(input("Introduzca el valor en letra de lo que deseé: ")).lower()

        if seleccionOpcion == "a":

            aprobadosExamen(alumnos,notas)

        elif seleccionOpcion == "b":

            numeroAprobados(notas)

        elif seleccionOpcion == "c":
            maximaNota(alumnos,notas)

        elif seleccionOpcion == "d":

            calificacionSuperiorIgualMedia(notas,alumnos)

        elif seleccionOpcion == "e":

            encontrarNombreAlumno(notas, alumnos, cadenaU)

        elif seleccionOpcion == "f":

            ordena_alumnes(alumnos,notas)

        elif seleccionOpcion == "g":

            terminar()

            menuSeguir = False

        else:
            menuSeguir = False
            return "No ha escogido una opción válida, acabamos el programa."


def aprobadosExamen(listaAlumnos, listaNotas):

    alumnosAprobados = []

    for i in range(len(listaNotas)):

        if listaNotas[i] >= 5.0:

            alumnosAprobados.append(listaAlumnos[i])

    print(f"Los alumnos aprobados serán {alumnosAprobados}")

def numeroAprobados(listaNotas):

    numAprobados = 0

    for i in range(len(listaNotas)):

        if listaNotas[i]>=5:

            numAprobados += 1

    print(f"El número de alumnos aprobados será de ***{numAprobados}*** alumnos aprobados")

def maximaNota(alumnos, notas):
    max_nota = max(notas)

    print("Alumnes amb la màxima nota:", max_nota)

    for i in range(len(alumnos)):

        if notas[i] == max_nota:
            print(alumnos[i])

def calificacionSuperiorIgualMedia(listaNotas,listaAlumnos):

    alumnosSuperiorMedia = []

    contadorNotas = 0

    sumaNotasTotal = 0.0

    mediaNotas = 0.0

    for i in range(len(listaNotas)):

        contadorNotas += 1

    sumaNotasTotal = sum(listaNotas)

    mediaNotas = sumaNotasTotal / contadorNotas

    print(f"\nLa nota media de todos los alumnos será igual a {mediaNotas}")

    for j in range(len(listaNotas)):

        if listaNotas[j] > mediaNotas:

            alumnosSuperiorMedia.append(listaAlumnos[j])

    print(f"Los alumnos que superan esta media son -> {alumnosSuperiorMedia}")

def encontrarNombreAlumno(listaNotas,listaAlumnos,cadenaUsuario):
    if cadenaUsuario in listaAlumnos:
        posicionAlumno = listaAlumnos.index(cadenaUsuario)
        print(listaNotas[posicionAlumno])

    else:
        print(None)

def ordena_alumnes(alumnos, notas):
    n = len(alumnos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if notas[j] < notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
    print("Alumnes ordenats per nota (de més alta a més baixa):")

    for j in range(len(alumnos)):
        print(alumnos[j], "-", notas[j])

def terminar():

    print("Saliendo del Programa...")

menuPrincipal()
print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)