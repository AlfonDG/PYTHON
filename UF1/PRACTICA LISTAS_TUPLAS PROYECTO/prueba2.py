print("***FALTA MEJORAR***")

listaProyectos = [("Proyecto1","Alfonso"), ("Proyecto2","Cristian")]

for i in range(len(listaProyectos)):

    if len(listaProyectos[0]) < 2:
        print(f"No quedan alumnos en el proyecto {listaProyectos[0::2]}... Por lo que procederemos a eliminar el grupo vacío\n")
        del listaProyectos[0]
        print(listaProyectos)

    elif len(listaProyectos[1]) < 2:
        print(f"No quedan alumnos en el proyecto {listaProyectos[0::2]}... Por lo que procederemos a eliminar el grupo vacío\n")
        del listaProyectos[1]
        print(listaProyectos)

    else:
        print("Los grupos tienen sus respectivos grupos. Procedemos a eliminar a un usuario del grupo\n")
        elegirAlumnoBorrar = str(input("Introduzca el usuario que desea borrar: "))

        if elegirAlumnoBorrar in listaProyectos[0][i + 1::]:
            print(f"Hemos encontrado al alumno... {listaProyectos[0][i + 1::]} Procedemos a borrarlo de la lista de proyectos")

            listaAisladaEliminarAlumno = list(listaProyectos[0][i + 1::])

            listaAisladaEliminarAlumno.pop(0)

            print(listaProyectos)

        elif elegirAlumnoBorrar in listaProyectos[1][i + 1::]:
            print(f"Hemos encontrado al alumno... {listaProyectos[1][i + 1::]} Procedemos a borrarlo de la lista de proyectos")
            listaAisladaEliminarAlumno = list(listaProyectos[1][i + 1::])

            listaAisladaEliminarAlumno.pop(0)

            print(listaProyectos)
        else:
            print(f"No hemos encontrado al alumno {elegirAlumnoBorrar} que has escrito")